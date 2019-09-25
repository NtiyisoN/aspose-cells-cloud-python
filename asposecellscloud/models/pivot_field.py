# coding: utf-8

"""
Copyright (c) 2019 Aspose.Cells Cloud
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
"""


from pprint import pformat
from six import iteritems
import re


class PivotField(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pivot_items': 'list[PivotItem]',
        'display_name': 'str',
        'number_format': 'str',
        'drag_to_column': 'bool',
        'is_auto_show': 'bool',
        'is_repeat_item_labels': 'bool',
        'drag_to_row': 'bool',
        'is_auto_sort': 'bool',
        'insert_blank_row': 'bool',
        'show_subtotal_at_top': 'bool',
        'show_compact': 'bool',
        'function': 'str',
        'is_multiple_item_selection_allowed': 'bool',
        'data_display_format': 'str',
        'base_item_position': 'str',
        'is_insert_page_breaks_between_items': 'bool',
        'show_all_items': 'bool',
        'base_item': 'int',
        'item_count': 'int',
        'name': 'str',
        'show_in_outline_form': 'bool',
        'items': 'list[str]',
        'auto_show_field': 'int',
        'is_auto_subtotals': 'bool',
        'is_include_new_items_in_filter': 'bool',
        'current_page_item': 'int',
        'position': 'int',
        'is_ascend_sort': 'bool',
        'is_ascend_show': 'bool',
        'base_field': 'int',
        'auto_sort_field': 'int',
        'auto_show_count': 'int',
        'number': 'int',
        'drag_to_page': 'bool',
        'drag_to_data': 'bool',
        'base_index': 'int',
        'original_items': 'list[str]',
        'drag_to_hide': 'bool',
        'is_calculated_field': 'bool'
    }

    attribute_map = {
        'pivot_items': 'PivotItems',
        'display_name': 'DisplayName',
        'number_format': 'NumberFormat',
        'drag_to_column': 'DragToColumn',
        'is_auto_show': 'IsAutoShow',
        'is_repeat_item_labels': 'IsRepeatItemLabels',
        'drag_to_row': 'DragToRow',
        'is_auto_sort': 'IsAutoSort',
        'insert_blank_row': 'InsertBlankRow',
        'show_subtotal_at_top': 'ShowSubtotalAtTop',
        'show_compact': 'ShowCompact',
        'function': 'Function',
        'is_multiple_item_selection_allowed': 'IsMultipleItemSelectionAllowed',
        'data_display_format': 'DataDisplayFormat',
        'base_item_position': 'BaseItemPosition',
        'is_insert_page_breaks_between_items': 'IsInsertPageBreaksBetweenItems',
        'show_all_items': 'ShowAllItems',
        'base_item': 'BaseItem',
        'item_count': 'ItemCount',
        'name': 'Name',
        'show_in_outline_form': 'ShowInOutlineForm',
        'items': 'Items',
        'auto_show_field': 'AutoShowField',
        'is_auto_subtotals': 'IsAutoSubtotals',
        'is_include_new_items_in_filter': 'IsIncludeNewItemsInFilter',
        'current_page_item': 'CurrentPageItem',
        'position': 'Position',
        'is_ascend_sort': 'IsAscendSort',
        'is_ascend_show': 'IsAscendShow',
        'base_field': 'BaseField',
        'auto_sort_field': 'AutoSortField',
        'auto_show_count': 'AutoShowCount',
        'number': 'Number',
        'drag_to_page': 'DragToPage',
        'drag_to_data': 'DragToData',
        'base_index': 'BaseIndex',
        'original_items': 'OriginalItems',
        'drag_to_hide': 'DragToHide',
        'is_calculated_field': 'IsCalculatedField'
    }
    
    @staticmethod
    def get_swagger_types():
        return PivotField.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return PivotField.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, pivot_items=None, display_name=None, number_format=None, drag_to_column=None, is_auto_show=None, is_repeat_item_labels=None, drag_to_row=None, is_auto_sort=None, insert_blank_row=None, show_subtotal_at_top=None, show_compact=None, function=None, is_multiple_item_selection_allowed=None, data_display_format=None, base_item_position=None, is_insert_page_breaks_between_items=None, show_all_items=None, base_item=None, item_count=None, name=None, show_in_outline_form=None, items=None, auto_show_field=None, is_auto_subtotals=None, is_include_new_items_in_filter=None, current_page_item=None, position=None, is_ascend_sort=None, is_ascend_show=None, base_field=None, auto_sort_field=None, auto_show_count=None, number=None, drag_to_page=None, drag_to_data=None, base_index=None, original_items=None, drag_to_hide=None, is_calculated_field=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        PivotField - a model defined in Swagger
        """

        self.container['pivot_items'] = None
        self.container['display_name'] = None
        self.container['number_format'] = None
        self.container['drag_to_column'] = None
        self.container['is_auto_show'] = None
        self.container['is_repeat_item_labels'] = None
        self.container['drag_to_row'] = None
        self.container['is_auto_sort'] = None
        self.container['insert_blank_row'] = None
        self.container['show_subtotal_at_top'] = None
        self.container['show_compact'] = None
        self.container['function'] = None
        self.container['is_multiple_item_selection_allowed'] = None
        self.container['data_display_format'] = None
        self.container['base_item_position'] = None
        self.container['is_insert_page_breaks_between_items'] = None
        self.container['show_all_items'] = None
        self.container['base_item'] = None
        self.container['item_count'] = None
        self.container['name'] = None
        self.container['show_in_outline_form'] = None
        self.container['items'] = None
        self.container['auto_show_field'] = None
        self.container['is_auto_subtotals'] = None
        self.container['is_include_new_items_in_filter'] = None
        self.container['current_page_item'] = None
        self.container['position'] = None
        self.container['is_ascend_sort'] = None
        self.container['is_ascend_show'] = None
        self.container['base_field'] = None
        self.container['auto_sort_field'] = None
        self.container['auto_show_count'] = None
        self.container['number'] = None
        self.container['drag_to_page'] = None
        self.container['drag_to_data'] = None
        self.container['base_index'] = None
        self.container['original_items'] = None
        self.container['drag_to_hide'] = None
        self.container['is_calculated_field'] = None

        if pivot_items is not None:
          self.pivot_items = pivot_items
        if display_name is not None:
          self.display_name = display_name
        if number_format is not None:
          self.number_format = number_format
        if drag_to_column is not None:
          self.drag_to_column = drag_to_column
        if is_auto_show is not None:
          self.is_auto_show = is_auto_show
        if is_repeat_item_labels is not None:
          self.is_repeat_item_labels = is_repeat_item_labels
        if drag_to_row is not None:
          self.drag_to_row = drag_to_row
        if is_auto_sort is not None:
          self.is_auto_sort = is_auto_sort
        if insert_blank_row is not None:
          self.insert_blank_row = insert_blank_row
        if show_subtotal_at_top is not None:
          self.show_subtotal_at_top = show_subtotal_at_top
        if show_compact is not None:
          self.show_compact = show_compact
        if function is not None:
          self.function = function
        if is_multiple_item_selection_allowed is not None:
          self.is_multiple_item_selection_allowed = is_multiple_item_selection_allowed
        if data_display_format is not None:
          self.data_display_format = data_display_format
        if base_item_position is not None:
          self.base_item_position = base_item_position
        if is_insert_page_breaks_between_items is not None:
          self.is_insert_page_breaks_between_items = is_insert_page_breaks_between_items
        if show_all_items is not None:
          self.show_all_items = show_all_items
        if base_item is not None:
          self.base_item = base_item
        if item_count is not None:
          self.item_count = item_count
        if name is not None:
          self.name = name
        if show_in_outline_form is not None:
          self.show_in_outline_form = show_in_outline_form
        if items is not None:
          self.items = items
        if auto_show_field is not None:
          self.auto_show_field = auto_show_field
        if is_auto_subtotals is not None:
          self.is_auto_subtotals = is_auto_subtotals
        if is_include_new_items_in_filter is not None:
          self.is_include_new_items_in_filter = is_include_new_items_in_filter
        if current_page_item is not None:
          self.current_page_item = current_page_item
        if position is not None:
          self.position = position
        if is_ascend_sort is not None:
          self.is_ascend_sort = is_ascend_sort
        if is_ascend_show is not None:
          self.is_ascend_show = is_ascend_show
        if base_field is not None:
          self.base_field = base_field
        if auto_sort_field is not None:
          self.auto_sort_field = auto_sort_field
        if auto_show_count is not None:
          self.auto_show_count = auto_show_count
        if number is not None:
          self.number = number
        if drag_to_page is not None:
          self.drag_to_page = drag_to_page
        if drag_to_data is not None:
          self.drag_to_data = drag_to_data
        if base_index is not None:
          self.base_index = base_index
        if original_items is not None:
          self.original_items = original_items
        if drag_to_hide is not None:
          self.drag_to_hide = drag_to_hide
        if is_calculated_field is not None:
          self.is_calculated_field = is_calculated_field

    @property
    def pivot_items(self):
        """
        Gets the pivot_items of this PivotField.

        :return: The pivot_items of this PivotField.
        :rtype: list[PivotItem]
        """
        return self.container['pivot_items']

    @pivot_items.setter
    def pivot_items(self, pivot_items):
        """
        Sets the pivot_items of this PivotField.

        :param pivot_items: The pivot_items of this PivotField.
        :type: list[PivotItem]
        """

        self.container['pivot_items'] = pivot_items

    @property
    def display_name(self):
        """
        Gets the display_name of this PivotField.

        :return: The display_name of this PivotField.
        :rtype: str
        """
        return self.container['display_name']

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PivotField.

        :param display_name: The display_name of this PivotField.
        :type: str
        """

        self.container['display_name'] = display_name

    @property
    def number_format(self):
        """
        Gets the number_format of this PivotField.

        :return: The number_format of this PivotField.
        :rtype: str
        """
        return self.container['number_format']

    @number_format.setter
    def number_format(self, number_format):
        """
        Sets the number_format of this PivotField.

        :param number_format: The number_format of this PivotField.
        :type: str
        """

        self.container['number_format'] = number_format

    @property
    def drag_to_column(self):
        """
        Gets the drag_to_column of this PivotField.

        :return: The drag_to_column of this PivotField.
        :rtype: bool
        """
        return self.container['drag_to_column']

    @drag_to_column.setter
    def drag_to_column(self, drag_to_column):
        """
        Sets the drag_to_column of this PivotField.

        :param drag_to_column: The drag_to_column of this PivotField.
        :type: bool
        """

        self.container['drag_to_column'] = drag_to_column

    @property
    def is_auto_show(self):
        """
        Gets the is_auto_show of this PivotField.

        :return: The is_auto_show of this PivotField.
        :rtype: bool
        """
        return self.container['is_auto_show']

    @is_auto_show.setter
    def is_auto_show(self, is_auto_show):
        """
        Sets the is_auto_show of this PivotField.

        :param is_auto_show: The is_auto_show of this PivotField.
        :type: bool
        """

        self.container['is_auto_show'] = is_auto_show

    @property
    def is_repeat_item_labels(self):
        """
        Gets the is_repeat_item_labels of this PivotField.

        :return: The is_repeat_item_labels of this PivotField.
        :rtype: bool
        """
        return self.container['is_repeat_item_labels']

    @is_repeat_item_labels.setter
    def is_repeat_item_labels(self, is_repeat_item_labels):
        """
        Sets the is_repeat_item_labels of this PivotField.

        :param is_repeat_item_labels: The is_repeat_item_labels of this PivotField.
        :type: bool
        """

        self.container['is_repeat_item_labels'] = is_repeat_item_labels

    @property
    def drag_to_row(self):
        """
        Gets the drag_to_row of this PivotField.

        :return: The drag_to_row of this PivotField.
        :rtype: bool
        """
        return self.container['drag_to_row']

    @drag_to_row.setter
    def drag_to_row(self, drag_to_row):
        """
        Sets the drag_to_row of this PivotField.

        :param drag_to_row: The drag_to_row of this PivotField.
        :type: bool
        """

        self.container['drag_to_row'] = drag_to_row

    @property
    def is_auto_sort(self):
        """
        Gets the is_auto_sort of this PivotField.

        :return: The is_auto_sort of this PivotField.
        :rtype: bool
        """
        return self.container['is_auto_sort']

    @is_auto_sort.setter
    def is_auto_sort(self, is_auto_sort):
        """
        Sets the is_auto_sort of this PivotField.

        :param is_auto_sort: The is_auto_sort of this PivotField.
        :type: bool
        """

        self.container['is_auto_sort'] = is_auto_sort

    @property
    def insert_blank_row(self):
        """
        Gets the insert_blank_row of this PivotField.

        :return: The insert_blank_row of this PivotField.
        :rtype: bool
        """
        return self.container['insert_blank_row']

    @insert_blank_row.setter
    def insert_blank_row(self, insert_blank_row):
        """
        Sets the insert_blank_row of this PivotField.

        :param insert_blank_row: The insert_blank_row of this PivotField.
        :type: bool
        """

        self.container['insert_blank_row'] = insert_blank_row

    @property
    def show_subtotal_at_top(self):
        """
        Gets the show_subtotal_at_top of this PivotField.

        :return: The show_subtotal_at_top of this PivotField.
        :rtype: bool
        """
        return self.container['show_subtotal_at_top']

    @show_subtotal_at_top.setter
    def show_subtotal_at_top(self, show_subtotal_at_top):
        """
        Sets the show_subtotal_at_top of this PivotField.

        :param show_subtotal_at_top: The show_subtotal_at_top of this PivotField.
        :type: bool
        """

        self.container['show_subtotal_at_top'] = show_subtotal_at_top

    @property
    def show_compact(self):
        """
        Gets the show_compact of this PivotField.

        :return: The show_compact of this PivotField.
        :rtype: bool
        """
        return self.container['show_compact']

    @show_compact.setter
    def show_compact(self, show_compact):
        """
        Sets the show_compact of this PivotField.

        :param show_compact: The show_compact of this PivotField.
        :type: bool
        """

        self.container['show_compact'] = show_compact

    @property
    def function(self):
        """
        Gets the function of this PivotField.

        :return: The function of this PivotField.
        :rtype: str
        """
        return self.container['function']

    @function.setter
    def function(self, function):
        """
        Sets the function of this PivotField.

        :param function: The function of this PivotField.
        :type: str
        """

        self.container['function'] = function

    @property
    def is_multiple_item_selection_allowed(self):
        """
        Gets the is_multiple_item_selection_allowed of this PivotField.

        :return: The is_multiple_item_selection_allowed of this PivotField.
        :rtype: bool
        """
        return self.container['is_multiple_item_selection_allowed']

    @is_multiple_item_selection_allowed.setter
    def is_multiple_item_selection_allowed(self, is_multiple_item_selection_allowed):
        """
        Sets the is_multiple_item_selection_allowed of this PivotField.

        :param is_multiple_item_selection_allowed: The is_multiple_item_selection_allowed of this PivotField.
        :type: bool
        """

        self.container['is_multiple_item_selection_allowed'] = is_multiple_item_selection_allowed

    @property
    def data_display_format(self):
        """
        Gets the data_display_format of this PivotField.

        :return: The data_display_format of this PivotField.
        :rtype: str
        """
        return self.container['data_display_format']

    @data_display_format.setter
    def data_display_format(self, data_display_format):
        """
        Sets the data_display_format of this PivotField.

        :param data_display_format: The data_display_format of this PivotField.
        :type: str
        """

        self.container['data_display_format'] = data_display_format

    @property
    def base_item_position(self):
        """
        Gets the base_item_position of this PivotField.

        :return: The base_item_position of this PivotField.
        :rtype: str
        """
        return self.container['base_item_position']

    @base_item_position.setter
    def base_item_position(self, base_item_position):
        """
        Sets the base_item_position of this PivotField.

        :param base_item_position: The base_item_position of this PivotField.
        :type: str
        """

        self.container['base_item_position'] = base_item_position

    @property
    def is_insert_page_breaks_between_items(self):
        """
        Gets the is_insert_page_breaks_between_items of this PivotField.

        :return: The is_insert_page_breaks_between_items of this PivotField.
        :rtype: bool
        """
        return self.container['is_insert_page_breaks_between_items']

    @is_insert_page_breaks_between_items.setter
    def is_insert_page_breaks_between_items(self, is_insert_page_breaks_between_items):
        """
        Sets the is_insert_page_breaks_between_items of this PivotField.

        :param is_insert_page_breaks_between_items: The is_insert_page_breaks_between_items of this PivotField.
        :type: bool
        """

        self.container['is_insert_page_breaks_between_items'] = is_insert_page_breaks_between_items

    @property
    def show_all_items(self):
        """
        Gets the show_all_items of this PivotField.

        :return: The show_all_items of this PivotField.
        :rtype: bool
        """
        return self.container['show_all_items']

    @show_all_items.setter
    def show_all_items(self, show_all_items):
        """
        Sets the show_all_items of this PivotField.

        :param show_all_items: The show_all_items of this PivotField.
        :type: bool
        """

        self.container['show_all_items'] = show_all_items

    @property
    def base_item(self):
        """
        Gets the base_item of this PivotField.

        :return: The base_item of this PivotField.
        :rtype: int
        """
        return self.container['base_item']

    @base_item.setter
    def base_item(self, base_item):
        """
        Sets the base_item of this PivotField.

        :param base_item: The base_item of this PivotField.
        :type: int
        """

        self.container['base_item'] = base_item

    @property
    def item_count(self):
        """
        Gets the item_count of this PivotField.

        :return: The item_count of this PivotField.
        :rtype: int
        """
        return self.container['item_count']

    @item_count.setter
    def item_count(self, item_count):
        """
        Sets the item_count of this PivotField.

        :param item_count: The item_count of this PivotField.
        :type: int
        """

        self.container['item_count'] = item_count

    @property
    def name(self):
        """
        Gets the name of this PivotField.

        :return: The name of this PivotField.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this PivotField.

        :param name: The name of this PivotField.
        :type: str
        """

        self.container['name'] = name

    @property
    def show_in_outline_form(self):
        """
        Gets the show_in_outline_form of this PivotField.

        :return: The show_in_outline_form of this PivotField.
        :rtype: bool
        """
        return self.container['show_in_outline_form']

    @show_in_outline_form.setter
    def show_in_outline_form(self, show_in_outline_form):
        """
        Sets the show_in_outline_form of this PivotField.

        :param show_in_outline_form: The show_in_outline_form of this PivotField.
        :type: bool
        """

        self.container['show_in_outline_form'] = show_in_outline_form

    @property
    def items(self):
        """
        Gets the items of this PivotField.

        :return: The items of this PivotField.
        :rtype: list[str]
        """
        return self.container['items']

    @items.setter
    def items(self, items):
        """
        Sets the items of this PivotField.

        :param items: The items of this PivotField.
        :type: list[str]
        """

        self.container['items'] = items

    @property
    def auto_show_field(self):
        """
        Gets the auto_show_field of this PivotField.

        :return: The auto_show_field of this PivotField.
        :rtype: int
        """
        return self.container['auto_show_field']

    @auto_show_field.setter
    def auto_show_field(self, auto_show_field):
        """
        Sets the auto_show_field of this PivotField.

        :param auto_show_field: The auto_show_field of this PivotField.
        :type: int
        """

        self.container['auto_show_field'] = auto_show_field

    @property
    def is_auto_subtotals(self):
        """
        Gets the is_auto_subtotals of this PivotField.

        :return: The is_auto_subtotals of this PivotField.
        :rtype: bool
        """
        return self.container['is_auto_subtotals']

    @is_auto_subtotals.setter
    def is_auto_subtotals(self, is_auto_subtotals):
        """
        Sets the is_auto_subtotals of this PivotField.

        :param is_auto_subtotals: The is_auto_subtotals of this PivotField.
        :type: bool
        """

        self.container['is_auto_subtotals'] = is_auto_subtotals

    @property
    def is_include_new_items_in_filter(self):
        """
        Gets the is_include_new_items_in_filter of this PivotField.

        :return: The is_include_new_items_in_filter of this PivotField.
        :rtype: bool
        """
        return self.container['is_include_new_items_in_filter']

    @is_include_new_items_in_filter.setter
    def is_include_new_items_in_filter(self, is_include_new_items_in_filter):
        """
        Sets the is_include_new_items_in_filter of this PivotField.

        :param is_include_new_items_in_filter: The is_include_new_items_in_filter of this PivotField.
        :type: bool
        """

        self.container['is_include_new_items_in_filter'] = is_include_new_items_in_filter

    @property
    def current_page_item(self):
        """
        Gets the current_page_item of this PivotField.

        :return: The current_page_item of this PivotField.
        :rtype: int
        """
        return self.container['current_page_item']

    @current_page_item.setter
    def current_page_item(self, current_page_item):
        """
        Sets the current_page_item of this PivotField.

        :param current_page_item: The current_page_item of this PivotField.
        :type: int
        """

        self.container['current_page_item'] = current_page_item

    @property
    def position(self):
        """
        Gets the position of this PivotField.

        :return: The position of this PivotField.
        :rtype: int
        """
        return self.container['position']

    @position.setter
    def position(self, position):
        """
        Sets the position of this PivotField.

        :param position: The position of this PivotField.
        :type: int
        """

        self.container['position'] = position

    @property
    def is_ascend_sort(self):
        """
        Gets the is_ascend_sort of this PivotField.

        :return: The is_ascend_sort of this PivotField.
        :rtype: bool
        """
        return self.container['is_ascend_sort']

    @is_ascend_sort.setter
    def is_ascend_sort(self, is_ascend_sort):
        """
        Sets the is_ascend_sort of this PivotField.

        :param is_ascend_sort: The is_ascend_sort of this PivotField.
        :type: bool
        """

        self.container['is_ascend_sort'] = is_ascend_sort

    @property
    def is_ascend_show(self):
        """
        Gets the is_ascend_show of this PivotField.

        :return: The is_ascend_show of this PivotField.
        :rtype: bool
        """
        return self.container['is_ascend_show']

    @is_ascend_show.setter
    def is_ascend_show(self, is_ascend_show):
        """
        Sets the is_ascend_show of this PivotField.

        :param is_ascend_show: The is_ascend_show of this PivotField.
        :type: bool
        """

        self.container['is_ascend_show'] = is_ascend_show

    @property
    def base_field(self):
        """
        Gets the base_field of this PivotField.

        :return: The base_field of this PivotField.
        :rtype: int
        """
        return self.container['base_field']

    @base_field.setter
    def base_field(self, base_field):
        """
        Sets the base_field of this PivotField.

        :param base_field: The base_field of this PivotField.
        :type: int
        """

        self.container['base_field'] = base_field

    @property
    def auto_sort_field(self):
        """
        Gets the auto_sort_field of this PivotField.

        :return: The auto_sort_field of this PivotField.
        :rtype: int
        """
        return self.container['auto_sort_field']

    @auto_sort_field.setter
    def auto_sort_field(self, auto_sort_field):
        """
        Sets the auto_sort_field of this PivotField.

        :param auto_sort_field: The auto_sort_field of this PivotField.
        :type: int
        """

        self.container['auto_sort_field'] = auto_sort_field

    @property
    def auto_show_count(self):
        """
        Gets the auto_show_count of this PivotField.

        :return: The auto_show_count of this PivotField.
        :rtype: int
        """
        return self.container['auto_show_count']

    @auto_show_count.setter
    def auto_show_count(self, auto_show_count):
        """
        Sets the auto_show_count of this PivotField.

        :param auto_show_count: The auto_show_count of this PivotField.
        :type: int
        """

        self.container['auto_show_count'] = auto_show_count

    @property
    def number(self):
        """
        Gets the number of this PivotField.

        :return: The number of this PivotField.
        :rtype: int
        """
        return self.container['number']

    @number.setter
    def number(self, number):
        """
        Sets the number of this PivotField.

        :param number: The number of this PivotField.
        :type: int
        """

        self.container['number'] = number

    @property
    def drag_to_page(self):
        """
        Gets the drag_to_page of this PivotField.

        :return: The drag_to_page of this PivotField.
        :rtype: bool
        """
        return self.container['drag_to_page']

    @drag_to_page.setter
    def drag_to_page(self, drag_to_page):
        """
        Sets the drag_to_page of this PivotField.

        :param drag_to_page: The drag_to_page of this PivotField.
        :type: bool
        """

        self.container['drag_to_page'] = drag_to_page

    @property
    def drag_to_data(self):
        """
        Gets the drag_to_data of this PivotField.

        :return: The drag_to_data of this PivotField.
        :rtype: bool
        """
        return self.container['drag_to_data']

    @drag_to_data.setter
    def drag_to_data(self, drag_to_data):
        """
        Sets the drag_to_data of this PivotField.

        :param drag_to_data: The drag_to_data of this PivotField.
        :type: bool
        """

        self.container['drag_to_data'] = drag_to_data

    @property
    def base_index(self):
        """
        Gets the base_index of this PivotField.

        :return: The base_index of this PivotField.
        :rtype: int
        """
        return self.container['base_index']

    @base_index.setter
    def base_index(self, base_index):
        """
        Sets the base_index of this PivotField.

        :param base_index: The base_index of this PivotField.
        :type: int
        """

        self.container['base_index'] = base_index

    @property
    def original_items(self):
        """
        Gets the original_items of this PivotField.

        :return: The original_items of this PivotField.
        :rtype: list[str]
        """
        return self.container['original_items']

    @original_items.setter
    def original_items(self, original_items):
        """
        Sets the original_items of this PivotField.

        :param original_items: The original_items of this PivotField.
        :type: list[str]
        """

        self.container['original_items'] = original_items

    @property
    def drag_to_hide(self):
        """
        Gets the drag_to_hide of this PivotField.

        :return: The drag_to_hide of this PivotField.
        :rtype: bool
        """
        return self.container['drag_to_hide']

    @drag_to_hide.setter
    def drag_to_hide(self, drag_to_hide):
        """
        Sets the drag_to_hide of this PivotField.

        :param drag_to_hide: The drag_to_hide of this PivotField.
        :type: bool
        """

        self.container['drag_to_hide'] = drag_to_hide

    @property
    def is_calculated_field(self):
        """
        Gets the is_calculated_field of this PivotField.

        :return: The is_calculated_field of this PivotField.
        :rtype: bool
        """
        return self.container['is_calculated_field']

    @is_calculated_field.setter
    def is_calculated_field(self, is_calculated_field):
        """
        Sets the is_calculated_field of this PivotField.

        :param is_calculated_field: The is_calculated_field of this PivotField.
        :type: bool
        """

        self.container['is_calculated_field'] = is_calculated_field

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PivotField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
