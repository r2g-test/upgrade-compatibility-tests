import unittest
from deep_tests.upgrade_model import IncompatibleChange, assert_non_destructive_required_change, negotiate, read_with_version


class Wave4SchemaDriftTests(unittest.TestCase):
    def test_negotiation_is_order_independent_and_rejects_disjoint_versions(self):
        self.assertEqual(negotiate([1, 3, 2], [2, 1, 3]), 3)
        self.assertEqual(negotiate([3, 2], [1, 2]), 2)
        with self.assertRaises(IncompatibleChange):
            negotiate([1], [2, 3])

    def test_old_reader_never_observes_future_nested_fields(self):
        record = {"version": 3, "id": "entity-1", "display_name": "current", "metadata": {"labels": ["b", "a"], "future_nested": {"secret": True}}, "status": "active", "future_top": [1, 2, 3]}
        self.assertEqual(read_with_version(record, 1), {"id": "entity-1", "name": "current"})

    def test_required_field_removal_fails_while_additive_shape_is_admitted(self):
        required = {"id", "display_name", "status"}
        assert_non_destructive_required_change(required, required)
        assert_non_destructive_required_change(required, required | {"metadata"})
        for removed in required:
            with self.assertRaises(IncompatibleChange):
                assert_non_destructive_required_change(required, required - {removed})

    def test_unknown_reader_version_fails_closed(self):
        record = {"version": 2, "id": "entity-2", "display_name": "v2", "labels": []}
        with self.assertRaises(IncompatibleChange):
            read_with_version(record, 99)


if __name__ == "__main__":
    unittest.main()
