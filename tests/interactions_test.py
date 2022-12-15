import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DragabblePage


@allure.suite('Interactions')
class TestInteractions:

    @allure.feature('Sortable')
    class TestSortablePage:

        @allure.title('Check Sortable')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert order_before != order_after, 'The order of the list has not been changed'
            assert grid_before != grid_after, 'The order of the grid has not been changed'

    @allure.feature('Selectable')
    class TestSelectablePage:

        @allure.title('Check Selectable')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, 'No elements were selected'
            assert len(item_grid) > 0, 'No elements were selected'

    @allure.feature('Resizable')
    class TestResizablePage:

        @allure.title('Check Resizable')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert max_box == ('250px', '270px'), 'Size not equal to "250px", "270px"'
            assert min_box == ('150px', '150px'), 'Size not equal to "150px", "150px"'
            assert max_resize != min_resize, 'Resizable hax not been changed'

    @allure.feature('Droppable')
    class TestDroppablePage:

        @allure.title('Check Simple Droppable')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', 'The elements has not been dropped'

        @allure.title('Check Accept Droppable')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == 'Drop here', 'The dropped element has been accepted'
            assert accept == 'Dropped!', 'The dropped element has not been accepted'

        @allure.title('Check Prevent Propogation Droppable')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', 'The elements texts has not been changed'
            assert not_greedy_inner == 'Dropped!', 'The elements texts has not been changed'
            assert greedy == 'Outer droppable', 'The elements texts has been changed'
            assert greedy_inner == 'Dropped!', 'The elements texts has not been changed'

        @allure.title('Check Revert Draggable Droppable')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_will_revert_draggable()
            not_will_after_move, not_will_after_revert = droppable_page.drop_not_will_revert_draggable()
            assert will_after_move != will_after_revert, 'The elements has not reverted'
            assert not_will_after_move == not_will_after_revert, 'The elements has reverted'

    @allure.feature('Dragabble')
    class TestDragabblePage:

        @allure.title('Check Simple Dragabble')
        def test_simple_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            before, after = dragabble_page.simple_drag_box()
            assert before != after, 'The position of the box has not been changed'

        @allure.title('Check Axis Restricted Dragabble')
        def test_axis_restricted_dragabble(self, driver):
            dragabble_page = DragabblePage(driver, 'https://demoqa.com/dragabble')
            dragabble_page.open()
            top_x, left_x = dragabble_page.axis_restricted_x()
            top_y, left_y = dragabble_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0, \
                'Box position has not changed or there has been a shift in the y-axis'
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0, \
                'Box position has not changed or there has been a shift in the y-axis'
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0, \
                'Box position has not changed or there has been a shift in the x-axis'
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0, \
                'Box position has not changed or there has been a shift in the x-axis'
