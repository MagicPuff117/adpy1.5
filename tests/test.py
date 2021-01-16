import unittest
from unittest.mock import patch
import json
import app
import os

documents = []
directories = {}


def setUpModule():
    with open(os.path.join('fixtures/documents.json')) as out_docs:
        documents.extend(json.load(out_docs))
    with open(os.path.join('fixtures/directories.json')) as out_dirs:
        directories.update(json.load(out_dirs))

@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestManageDocs(unittest.TestCase):
    def setUp(self) -> None:
        self.directories = directories
        self.documents = documents


    def test_add_doc_on_directories(self):
        len_doc = len(self.directories['2'])
        # self.assertEqual(len_doc, 1)

        app.append_doc_to_shelf('12345', '2')
        self.assertGreater(len(self.directories['2']), len_doc)

    def test_deleted_doc(self):
        len_doc = len(self.documents)
        len_dir = len(self.directories['1'])
        app.delete_doc()
        self.assertGreater(len_doc, len(self.documents))
        self.assertGreater(len_dir, len(self.directories['1']))

