import pytest
from unittest.mock import Mock, patch
from drone import arm, video, version_major, version_minor, check_battery, check_altitude, check_roll, check_pitch, check_velocity, check_airspeed, check_groundspeed, check_mode, check_is_armable, check_armed, check_temperature, check_status, check_parameters, check_gps, check_last_heartbeat, check_home_location, mission_check, compass_calibration, set_mode, set_status, set_mission, check_location_lat, check_location_lon, check_location_alt, make_guided, compass, make_arm, ground_speed

@patch('your_module.connect')
def test_arm(mock_connect):
    mock_vehicle = Mock()
    mock_connect.return_value = mock_vehicle
    mock_vehicle.is_armable = True
    mock_vehicle.armed = False
    arm()
    assert mock_vehicle.armed

@patch('your_module.cv2.VideoCapture')
def test_video(mock_video_capture):
    mock_video_capture.return_value = Mock(isOpened=lambda: False)
    with pytest.raises(SystemExit):
        video()

@patch('your_module.connect')
def test_version_major(mock_connect):
    mock_vehicle = Mock()
    mock_connect.return_value = mock_vehicle
    mock_vehicle.version.major = 3
    assert version_major() == 3

@patch('your_module.connect')
def test_version_minor(mock_connect):
    mock_vehicle = Mock()
    mock_connect.return_value = mock_vehicle
    mock_vehicle.version.minor = 5
    assert version_minor() == 5

# Add more tests for the remaining functions in a similar manner