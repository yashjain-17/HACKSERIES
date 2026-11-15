import unittest

from app import app, notes


class NotesApiTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()
        notes.clear()

    def test_health_routes_are_registered(self):
        for route, expected_message in (
            ("/", "API is running"),
            ("/test", "The test is working."),
        ):
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json()["message"], expected_message)

    def test_user_route_is_registered(self):
        response = self.client.get("/user")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["role"], "Developer")

    def test_note_create_read_update_delete(self):
        created = self.client.post("/addnote", json={"title": "First"})
        self.assertEqual(created.status_code, 201)
        self.assertEqual(self.client.get("/notes").get_json(), [{"title": "First"}])

        updated = self.client.put("/notes/0", json={"title": "Updated"})
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(self.client.get("/notes").get_json(), [{"title": "Updated"}])

        deleted = self.client.delete("/notes/0")
        self.assertEqual(deleted.status_code, 200)
        self.assertEqual(self.client.get("/notes").get_json(), [])

    def test_non_object_and_malformed_json_are_rejected(self):
        self.assertEqual(self.client.post("/addnote", json=[]).status_code, 400)
        malformed = self.client.post(
            "/addnote",
            data="{",
            content_type="application/json",
        )
        self.assertEqual(malformed.status_code, 400)
        self.assertEqual(
            self.client.put("/notes/0", json={"title": "Updated"}).status_code,
            404,
        )

    def test_invalid_indexes_are_rejected(self):
        self.assertEqual(self.client.put("/notes/-1", json={"title": "bad"}).status_code, 404)
        self.assertEqual(self.client.delete("/notes/5").status_code, 404)


if __name__ == "__main__":
    unittest.main()
