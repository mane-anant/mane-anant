from users.logic import data_songs
import json
import pytest
from users.models.Songs import Song


@pytest.mark.parametrize((
    'audioFileType_result',
    'status_code',
    'expected_result'
),(
    (
        1,200,
    {
        'id':1,
        'songname':'tera fitur',
        'duration':'3',
        'uploaded_date': '2022/05/27'
    }),
    (0,404, 'audio file not available'
    
    )
    ))
def test_getsongbytype(fixture_client,mocker,audioFileType_result,status_code,expected_result):
    audioFileType='song'
    get_song_mock =mocker.patch.object(data_songs,'get_data')
    get_song_mock.return_value = audioFileType_result
    handler_response = fixture_client.get('/get/audioFileType')
    result_data = None

    if handler_response.data.decode() != '':
        result_data = handler_response.data.decode()
        return result_data
    if handler_response.status_code != 404:
        assert get_song_mock.called
        get_song_mock.assert_called_with(
            audioFileType)

    assert handler_response.status_code == status_code
    assert result_data == expected_result

@pytest.mark.parametrize((
    'get_id','status_code',
    'expected_response'
),[
    (
        1,204,
        'Data deleted Successsully'
    ),
    (
        2,204,
        'Data deleted Successsully'
    ),
    (
        3,204,
        'Data deleted Successsully'
    ),
    (
         14,204,
        'Invalid INPUT'
    )
]
)
def test_delete_user_data(mocker,fixture_client,get_id,expected_response,status_code):
    audioFileType='song'
    delete_song_mock =mocker.patch.object(data_songs,'delete_data')
    delete_song_mock.return_value = expected_response
    handler_response = fixture_client.delete(f'/delete/{audioFileType}/{get_id}')
    # assert delete_song_mock.called
    assert delete_song_mock.called_with(audioFileType,get_id)
    # assert handler_response.status_code == status_code
    if handler_response.data.decode() != '':
        result_data = handler_response.data.decode()
        return result_data
    # result_data = handler_response.data.decode()
    assert handler_response.status_code == status_code
    assert result_data == expected_response
#####################################################################################
@pytest.mark.parametrize((
    'payload','expected_response'
),[
    (
        {'audioFileType':'song','audioFileMetaData':{'id': 1, 'name': 'tera fitur','Duration':3,'Uploaded_time':'2022/3/30'}},
        'Data submitted Successsully'
    ),
    (
        {'audioFileType':'song','audioFileMetaData':{'id': 2, 'name': 'tera fitur','Duration':3,'Uploaded_time':'2022/3/30'}},
        'Data submitted Successsully'
    ),
    (
        {'audioFileType':'song','audioFileMetaData':{'id': 3, 'name': 'tera fitur','Duration':3,'Uploaded_time':'2022/3/30'}},
        'Data submitted Successsully'
    ),
    (
        {'id': 1, 'name': 'nullwa','Duration':3,'Uploaded_time':'2022/3/30'},
        'Invalid Data'
    )
]
)
def test_add_user_data(mocker,fixture_client,payload,expected_response):
    create_song_mock =mocker.patch.object(data_songs,'add_data')
    create_song_mock.return_value = expected_response
    handler_response = fixture_client.post('/add',json=payload)
    if handler_response.data.decode() != '':
        result_data = handler_response.data.decode()
        return result_data
    # result_data = handler_response.data.decode()
    assert handler_response.status_code == 200
    if expected_response:
        # assert result_data == expected_response
        assert create_song_mock.called
        assert create_song_mock.call_args_list[0][0][0] == payload
        assert type(create_song_mock.call_args_list[0][0][1]) == str
    else:
        assert result_data == expected_response.errors
