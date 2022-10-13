import json
import unittest
import unittest.mock
from unittest.mock import patch
from unittest.mock import Mock
# from hw05a import getCommitnum, getUserRepos

import githubapi

class TestHw04a(unittest.TestCase):
        
    @patch("githubapi.githubapi",return_value=['Repo: api-development-tools  Number of commits: 30', 'Repo: assets  Number of assets:30'])
    #@patch.object(, "fetch_user_repo")
    def test_fetch_user_repo_mock_api(self, mock_fetch_user_repo):
        response_file = open('./response_fetch_user_repo.json')        
        repo_call_response = json.load(response_file)
        mock_fetch_user_repo.return_value = Mock(status_code = 200)
        mock_fetch_user_repo.return_value.json = repo_call_response
        response = githubapi.githubapi('NehharShah')
        #print(response)
        self.assertEqual(response.json[0]['name'],"chatbot_ner")
        response_file.close()
       


        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(exit=False)