import os



class unix_fs:
    @staticmethod
    def rm(filename):
        os.remove(filename)

def test_unix_fs(mocker):
    mocker.patch('os.remove')
    unix_fs.rm('file')
    os.remove.assert_called_once_with('file')

def test_foo(mocker):
    # all valid calls
    mocker.patch('os.remove')
    mocker.patch.object(os, 'listdir')
    mocked_isfile = mocker.patch('os.path.isfile')