def test_alert_reporting_zoome(australia_check_zoome):
    australia_check_zoome.casino_check()
    assert australia_check_zoome.check_result_sz()
    australia_check_zoome.close()


def test_alert_repoting_oxi(australia_check_oxi):
    australia_check_oxi.casino_check()
    assert australia_check_oxi.check_result_jr()
    australia_check_oxi.close()