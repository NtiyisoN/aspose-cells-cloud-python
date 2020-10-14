# coding: utf-8

"""
Copyright (c) 2020 Aspose.Cells Cloud
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


class SparklineGroup(object):
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
        'display_hidden': 'bool',
        'first_point_color': 'CellsColor',
        'high_point_color': 'CellsColor',
        'horizontal_axis_color': 'CellsColor',
        'horizontal_axis_date_range': 'str',
        'last_point_color': 'CellsColor',
        'line_weight': 'float',
        'low_point_color': 'CellsColor',
        'markers_color': 'CellsColor',
        'negative_points_color': 'CellsColor',
        'plot_empty_cells_type': 'str',
        'plot_right_to_left': 'bool',
        'preset_style': 'str',
        'series_color': 'CellsColor',
        'show_first_point': 'bool',
        'show_high_point': 'bool',
        'show_horizontal_axis': 'bool',
        'show_last_point': 'bool',
        'show_low_point': 'bool',
        'show_markers': 'bool',
        'show_negative_points': 'bool',
        'sparkline_collection': 'list[Sparkline]',
        'type': 'str',
        'vertical_axis_max_value': 'float',
        'vertical_axis_max_value_type': 'str',
        'vertical_axis_min_value': 'float',
        'vertical_axis_min_value_type': 'str'
    }

    attribute_map = {
        'display_hidden': 'DisplayHidden',
        'first_point_color': 'FirstPointColor',
        'high_point_color': 'HighPointColor',
        'horizontal_axis_color': 'HorizontalAxisColor',
        'horizontal_axis_date_range': 'HorizontalAxisDateRange',
        'last_point_color': 'LastPointColor',
        'line_weight': 'LineWeight',
        'low_point_color': 'LowPointColor',
        'markers_color': 'MarkersColor',
        'negative_points_color': 'NegativePointsColor',
        'plot_empty_cells_type': 'PlotEmptyCellsType',
        'plot_right_to_left': 'PlotRightToLeft',
        'preset_style': 'PresetStyle',
        'series_color': 'SeriesColor',
        'show_first_point': 'ShowFirstPoint',
        'show_high_point': 'ShowHighPoint',
        'show_horizontal_axis': 'ShowHorizontalAxis',
        'show_last_point': 'ShowLastPoint',
        'show_low_point': 'ShowLowPoint',
        'show_markers': 'ShowMarkers',
        'show_negative_points': 'ShowNegativePoints',
        'sparkline_collection': 'SparklineCollection',
        'type': 'Type',
        'vertical_axis_max_value': 'VerticalAxisMaxValue',
        'vertical_axis_max_value_type': 'VerticalAxisMaxValueType',
        'vertical_axis_min_value': 'VerticalAxisMinValue',
        'vertical_axis_min_value_type': 'VerticalAxisMinValueType'
    }
    
    @staticmethod
    def get_swagger_types():
        return SparklineGroup.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return SparklineGroup.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, display_hidden=None, first_point_color=None, high_point_color=None, horizontal_axis_color=None, horizontal_axis_date_range=None, last_point_color=None, line_weight=None, low_point_color=None, markers_color=None, negative_points_color=None, plot_empty_cells_type=None, plot_right_to_left=None, preset_style=None, series_color=None, show_first_point=None, show_high_point=None, show_horizontal_axis=None, show_last_point=None, show_low_point=None, show_markers=None, show_negative_points=None, sparkline_collection=None, type=None, vertical_axis_max_value=None, vertical_axis_max_value_type=None, vertical_axis_min_value=None, vertical_axis_min_value_type=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        SparklineGroup - a model defined in Swagger
        """

        self.container['display_hidden'] = None
        self.container['first_point_color'] = None
        self.container['high_point_color'] = None
        self.container['horizontal_axis_color'] = None
        self.container['horizontal_axis_date_range'] = None
        self.container['last_point_color'] = None
        self.container['line_weight'] = None
        self.container['low_point_color'] = None
        self.container['markers_color'] = None
        self.container['negative_points_color'] = None
        self.container['plot_empty_cells_type'] = None
        self.container['plot_right_to_left'] = None
        self.container['preset_style'] = None
        self.container['series_color'] = None
        self.container['show_first_point'] = None
        self.container['show_high_point'] = None
        self.container['show_horizontal_axis'] = None
        self.container['show_last_point'] = None
        self.container['show_low_point'] = None
        self.container['show_markers'] = None
        self.container['show_negative_points'] = None
        self.container['sparkline_collection'] = None
        self.container['type'] = None
        self.container['vertical_axis_max_value'] = None
        self.container['vertical_axis_max_value_type'] = None
        self.container['vertical_axis_min_value'] = None
        self.container['vertical_axis_min_value_type'] = None

        if display_hidden is not None:
          self.display_hidden = display_hidden
        if first_point_color is not None:
          self.first_point_color = first_point_color
        if high_point_color is not None:
          self.high_point_color = high_point_color
        if horizontal_axis_color is not None:
          self.horizontal_axis_color = horizontal_axis_color
        if horizontal_axis_date_range is not None:
          self.horizontal_axis_date_range = horizontal_axis_date_range
        if last_point_color is not None:
          self.last_point_color = last_point_color
        if line_weight is not None:
          self.line_weight = line_weight
        if low_point_color is not None:
          self.low_point_color = low_point_color
        if markers_color is not None:
          self.markers_color = markers_color
        if negative_points_color is not None:
          self.negative_points_color = negative_points_color
        if plot_empty_cells_type is not None:
          self.plot_empty_cells_type = plot_empty_cells_type
        if plot_right_to_left is not None:
          self.plot_right_to_left = plot_right_to_left
        if preset_style is not None:
          self.preset_style = preset_style
        if series_color is not None:
          self.series_color = series_color
        if show_first_point is not None:
          self.show_first_point = show_first_point
        if show_high_point is not None:
          self.show_high_point = show_high_point
        if show_horizontal_axis is not None:
          self.show_horizontal_axis = show_horizontal_axis
        if show_last_point is not None:
          self.show_last_point = show_last_point
        if show_low_point is not None:
          self.show_low_point = show_low_point
        if show_markers is not None:
          self.show_markers = show_markers
        if show_negative_points is not None:
          self.show_negative_points = show_negative_points
        if sparkline_collection is not None:
          self.sparkline_collection = sparkline_collection
        if type is not None:
          self.type = type
        if vertical_axis_max_value is not None:
          self.vertical_axis_max_value = vertical_axis_max_value
        if vertical_axis_max_value_type is not None:
          self.vertical_axis_max_value_type = vertical_axis_max_value_type
        if vertical_axis_min_value is not None:
          self.vertical_axis_min_value = vertical_axis_min_value
        if vertical_axis_min_value_type is not None:
          self.vertical_axis_min_value_type = vertical_axis_min_value_type

    @property
    def display_hidden(self):
        """
        Gets the display_hidden of this SparklineGroup.

        :return: The display_hidden of this SparklineGroup.
        :rtype: bool
        """
        return self.container['display_hidden']

    @display_hidden.setter
    def display_hidden(self, display_hidden):
        """
        Sets the display_hidden of this SparklineGroup.

        :param display_hidden: The display_hidden of this SparklineGroup.
        :type: bool
        """

        self.container['display_hidden'] = display_hidden

    @property
    def first_point_color(self):
        """
        Gets the first_point_color of this SparklineGroup.

        :return: The first_point_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['first_point_color']

    @first_point_color.setter
    def first_point_color(self, first_point_color):
        """
        Sets the first_point_color of this SparklineGroup.

        :param first_point_color: The first_point_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['first_point_color'] = first_point_color

    @property
    def high_point_color(self):
        """
        Gets the high_point_color of this SparklineGroup.

        :return: The high_point_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['high_point_color']

    @high_point_color.setter
    def high_point_color(self, high_point_color):
        """
        Sets the high_point_color of this SparklineGroup.

        :param high_point_color: The high_point_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['high_point_color'] = high_point_color

    @property
    def horizontal_axis_color(self):
        """
        Gets the horizontal_axis_color of this SparklineGroup.

        :return: The horizontal_axis_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['horizontal_axis_color']

    @horizontal_axis_color.setter
    def horizontal_axis_color(self, horizontal_axis_color):
        """
        Sets the horizontal_axis_color of this SparklineGroup.

        :param horizontal_axis_color: The horizontal_axis_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['horizontal_axis_color'] = horizontal_axis_color

    @property
    def horizontal_axis_date_range(self):
        """
        Gets the horizontal_axis_date_range of this SparklineGroup.

        :return: The horizontal_axis_date_range of this SparklineGroup.
        :rtype: str
        """
        return self.container['horizontal_axis_date_range']

    @horizontal_axis_date_range.setter
    def horizontal_axis_date_range(self, horizontal_axis_date_range):
        """
        Sets the horizontal_axis_date_range of this SparklineGroup.

        :param horizontal_axis_date_range: The horizontal_axis_date_range of this SparklineGroup.
        :type: str
        """

        self.container['horizontal_axis_date_range'] = horizontal_axis_date_range

    @property
    def last_point_color(self):
        """
        Gets the last_point_color of this SparklineGroup.

        :return: The last_point_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['last_point_color']

    @last_point_color.setter
    def last_point_color(self, last_point_color):
        """
        Sets the last_point_color of this SparklineGroup.

        :param last_point_color: The last_point_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['last_point_color'] = last_point_color

    @property
    def line_weight(self):
        """
        Gets the line_weight of this SparklineGroup.

        :return: The line_weight of this SparklineGroup.
        :rtype: float
        """
        return self.container['line_weight']

    @line_weight.setter
    def line_weight(self, line_weight):
        """
        Sets the line_weight of this SparklineGroup.

        :param line_weight: The line_weight of this SparklineGroup.
        :type: float
        """

        self.container['line_weight'] = line_weight

    @property
    def low_point_color(self):
        """
        Gets the low_point_color of this SparklineGroup.

        :return: The low_point_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['low_point_color']

    @low_point_color.setter
    def low_point_color(self, low_point_color):
        """
        Sets the low_point_color of this SparklineGroup.

        :param low_point_color: The low_point_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['low_point_color'] = low_point_color

    @property
    def markers_color(self):
        """
        Gets the markers_color of this SparklineGroup.

        :return: The markers_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['markers_color']

    @markers_color.setter
    def markers_color(self, markers_color):
        """
        Sets the markers_color of this SparklineGroup.

        :param markers_color: The markers_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['markers_color'] = markers_color

    @property
    def negative_points_color(self):
        """
        Gets the negative_points_color of this SparklineGroup.

        :return: The negative_points_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['negative_points_color']

    @negative_points_color.setter
    def negative_points_color(self, negative_points_color):
        """
        Sets the negative_points_color of this SparklineGroup.

        :param negative_points_color: The negative_points_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['negative_points_color'] = negative_points_color

    @property
    def plot_empty_cells_type(self):
        """
        Gets the plot_empty_cells_type of this SparklineGroup.

        :return: The plot_empty_cells_type of this SparklineGroup.
        :rtype: str
        """
        return self.container['plot_empty_cells_type']

    @plot_empty_cells_type.setter
    def plot_empty_cells_type(self, plot_empty_cells_type):
        """
        Sets the plot_empty_cells_type of this SparklineGroup.

        :param plot_empty_cells_type: The plot_empty_cells_type of this SparklineGroup.
        :type: str
        """

        self.container['plot_empty_cells_type'] = plot_empty_cells_type

    @property
    def plot_right_to_left(self):
        """
        Gets the plot_right_to_left of this SparklineGroup.

        :return: The plot_right_to_left of this SparklineGroup.
        :rtype: bool
        """
        return self.container['plot_right_to_left']

    @plot_right_to_left.setter
    def plot_right_to_left(self, plot_right_to_left):
        """
        Sets the plot_right_to_left of this SparklineGroup.

        :param plot_right_to_left: The plot_right_to_left of this SparklineGroup.
        :type: bool
        """

        self.container['plot_right_to_left'] = plot_right_to_left

    @property
    def preset_style(self):
        """
        Gets the preset_style of this SparklineGroup.

        :return: The preset_style of this SparklineGroup.
        :rtype: str
        """
        return self.container['preset_style']

    @preset_style.setter
    def preset_style(self, preset_style):
        """
        Sets the preset_style of this SparklineGroup.

        :param preset_style: The preset_style of this SparklineGroup.
        :type: str
        """

        self.container['preset_style'] = preset_style

    @property
    def series_color(self):
        """
        Gets the series_color of this SparklineGroup.

        :return: The series_color of this SparklineGroup.
        :rtype: CellsColor
        """
        return self.container['series_color']

    @series_color.setter
    def series_color(self, series_color):
        """
        Sets the series_color of this SparklineGroup.

        :param series_color: The series_color of this SparklineGroup.
        :type: CellsColor
        """

        self.container['series_color'] = series_color

    @property
    def show_first_point(self):
        """
        Gets the show_first_point of this SparklineGroup.

        :return: The show_first_point of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_first_point']

    @show_first_point.setter
    def show_first_point(self, show_first_point):
        """
        Sets the show_first_point of this SparklineGroup.

        :param show_first_point: The show_first_point of this SparklineGroup.
        :type: bool
        """

        self.container['show_first_point'] = show_first_point

    @property
    def show_high_point(self):
        """
        Gets the show_high_point of this SparklineGroup.

        :return: The show_high_point of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_high_point']

    @show_high_point.setter
    def show_high_point(self, show_high_point):
        """
        Sets the show_high_point of this SparklineGroup.

        :param show_high_point: The show_high_point of this SparklineGroup.
        :type: bool
        """

        self.container['show_high_point'] = show_high_point

    @property
    def show_horizontal_axis(self):
        """
        Gets the show_horizontal_axis of this SparklineGroup.

        :return: The show_horizontal_axis of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_horizontal_axis']

    @show_horizontal_axis.setter
    def show_horizontal_axis(self, show_horizontal_axis):
        """
        Sets the show_horizontal_axis of this SparklineGroup.

        :param show_horizontal_axis: The show_horizontal_axis of this SparklineGroup.
        :type: bool
        """

        self.container['show_horizontal_axis'] = show_horizontal_axis

    @property
    def show_last_point(self):
        """
        Gets the show_last_point of this SparklineGroup.

        :return: The show_last_point of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_last_point']

    @show_last_point.setter
    def show_last_point(self, show_last_point):
        """
        Sets the show_last_point of this SparklineGroup.

        :param show_last_point: The show_last_point of this SparklineGroup.
        :type: bool
        """

        self.container['show_last_point'] = show_last_point

    @property
    def show_low_point(self):
        """
        Gets the show_low_point of this SparklineGroup.

        :return: The show_low_point of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_low_point']

    @show_low_point.setter
    def show_low_point(self, show_low_point):
        """
        Sets the show_low_point of this SparklineGroup.

        :param show_low_point: The show_low_point of this SparklineGroup.
        :type: bool
        """

        self.container['show_low_point'] = show_low_point

    @property
    def show_markers(self):
        """
        Gets the show_markers of this SparklineGroup.

        :return: The show_markers of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_markers']

    @show_markers.setter
    def show_markers(self, show_markers):
        """
        Sets the show_markers of this SparklineGroup.

        :param show_markers: The show_markers of this SparklineGroup.
        :type: bool
        """

        self.container['show_markers'] = show_markers

    @property
    def show_negative_points(self):
        """
        Gets the show_negative_points of this SparklineGroup.

        :return: The show_negative_points of this SparklineGroup.
        :rtype: bool
        """
        return self.container['show_negative_points']

    @show_negative_points.setter
    def show_negative_points(self, show_negative_points):
        """
        Sets the show_negative_points of this SparklineGroup.

        :param show_negative_points: The show_negative_points of this SparklineGroup.
        :type: bool
        """

        self.container['show_negative_points'] = show_negative_points

    @property
    def sparkline_collection(self):
        """
        Gets the sparkline_collection of this SparklineGroup.

        :return: The sparkline_collection of this SparklineGroup.
        :rtype: list[Sparkline]
        """
        return self.container['sparkline_collection']

    @sparkline_collection.setter
    def sparkline_collection(self, sparkline_collection):
        """
        Sets the sparkline_collection of this SparklineGroup.

        :param sparkline_collection: The sparkline_collection of this SparklineGroup.
        :type: list[Sparkline]
        """

        self.container['sparkline_collection'] = sparkline_collection

    @property
    def type(self):
        """
        Gets the type of this SparklineGroup.

        :return: The type of this SparklineGroup.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this SparklineGroup.

        :param type: The type of this SparklineGroup.
        :type: str
        """

        self.container['type'] = type

    @property
    def vertical_axis_max_value(self):
        """
        Gets the vertical_axis_max_value of this SparklineGroup.

        :return: The vertical_axis_max_value of this SparklineGroup.
        :rtype: float
        """
        return self.container['vertical_axis_max_value']

    @vertical_axis_max_value.setter
    def vertical_axis_max_value(self, vertical_axis_max_value):
        """
        Sets the vertical_axis_max_value of this SparklineGroup.

        :param vertical_axis_max_value: The vertical_axis_max_value of this SparklineGroup.
        :type: float
        """

        self.container['vertical_axis_max_value'] = vertical_axis_max_value

    @property
    def vertical_axis_max_value_type(self):
        """
        Gets the vertical_axis_max_value_type of this SparklineGroup.

        :return: The vertical_axis_max_value_type of this SparklineGroup.
        :rtype: str
        """
        return self.container['vertical_axis_max_value_type']

    @vertical_axis_max_value_type.setter
    def vertical_axis_max_value_type(self, vertical_axis_max_value_type):
        """
        Sets the vertical_axis_max_value_type of this SparklineGroup.

        :param vertical_axis_max_value_type: The vertical_axis_max_value_type of this SparklineGroup.
        :type: str
        """

        self.container['vertical_axis_max_value_type'] = vertical_axis_max_value_type

    @property
    def vertical_axis_min_value(self):
        """
        Gets the vertical_axis_min_value of this SparklineGroup.

        :return: The vertical_axis_min_value of this SparklineGroup.
        :rtype: float
        """
        return self.container['vertical_axis_min_value']

    @vertical_axis_min_value.setter
    def vertical_axis_min_value(self, vertical_axis_min_value):
        """
        Sets the vertical_axis_min_value of this SparklineGroup.

        :param vertical_axis_min_value: The vertical_axis_min_value of this SparklineGroup.
        :type: float
        """

        self.container['vertical_axis_min_value'] = vertical_axis_min_value

    @property
    def vertical_axis_min_value_type(self):
        """
        Gets the vertical_axis_min_value_type of this SparklineGroup.

        :return: The vertical_axis_min_value_type of this SparklineGroup.
        :rtype: str
        """
        return self.container['vertical_axis_min_value_type']

    @vertical_axis_min_value_type.setter
    def vertical_axis_min_value_type(self, vertical_axis_min_value_type):
        """
        Sets the vertical_axis_min_value_type of this SparklineGroup.

        :param vertical_axis_min_value_type: The vertical_axis_min_value_type of this SparklineGroup.
        :type: str
        """

        self.container['vertical_axis_min_value_type'] = vertical_axis_min_value_type

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
        if not isinstance(other, SparklineGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other