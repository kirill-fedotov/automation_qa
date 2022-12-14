import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, FramesPage, NestedFramesPage, ModalDialogsPage
from pages.alerts_frame_windows_page import AlertsPage


@allure.suite('Alerts, Frame, Windows')
class TestAlertsFrameWindows:

    @allure.feature('BrowserWindows')
    class TestBrowserWindows:

        @allure.title('Check New Tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', 'The new tab has not opened or an incorrect tab has opened'

        @allure.title('Check New Window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            assert text_result == 'This is a sample page', \
                'The new window has not opened or an incorrect window has opened'

    @allure.feature('Alerts')
    class TestAlertsPage:

        @allure.title('Check See Alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_window_text = alert_page.check_see_alert()
            assert alert_window_text == 'You clicked a button', 'Alert did not show up'

        @allure.title('Check Alert Appear (5 sec)')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_window_text = alert_page.check_alert_appear_5_sec()
            assert alert_window_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        @allure.title('Check Confirm Alert')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_window_text = alert_page.check_confirm_alert()
            assert alert_window_text == 'You selected Ok', 'Alert did not show up'

        @allure.title('Check Prompt Alert')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, text_result = alert_page.check_prompt_alert()
            assert text in text_result, 'Alert did not show up'
            # assert f"You entered {text}" == text_result

    @allure.feature('Frames')
    class TestFramesPage:

        @allure.title('Check Frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']

    @allure.feature('Check Nested Frames')
    class TestNestedFramesPage:

        @allure.title('Check Nested Frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialogs')
    class TestModalDialogsPage:

        @allure.title('Check Modal Dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[0] == 'Small Modal', 'The header is not "Small Modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large Modal"'
            assert small[1] < large[1], 'The text from the small dialogue is larger than the text from the large ' \
                                        'dialogue '


