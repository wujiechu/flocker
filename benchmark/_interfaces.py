# Copyright 2015 ClusterHQ Inc.  See LICENSE file for details.
"""
Operations for the control service benchmarks.
"""

from zope.interface import Interface


class IScenario(Interface):
    """
    A scenario in which an operation occurs.
    """

    def __init__(self, clock, control_service):
        """
        Provide the scenario with a clock and control service.
        """

    def start(self):
        """
        :return: A Deferred that fires when the desired scenario is
            established (e.g. that a certain load is being applied).
        """

    def maintained(self):
        """
        :return: A Deferred that fires with an errback if the desired
            scenario fails to hold between being established and being
            stopped.  This Deferred never fires with a callback.
        """

    def stop(self):
        """
        Stop the scenario from being maintained.

        :return: A Deferred that fires when the desired scenario is
            stopped.
        """


class IProbe(Interface):
    """A probe that performs an operation."""

    def run():
        """
        Run the operation.  This should run with as little overhead as
        possible, in order to ensure benchmark measurements are accurate.

        :return: A Deferred firing with the result of the operation.
        """

    def cleanup():
        """
        Perform any cleanup required after the operation.  This is performed
        outside the benchmark measurement.

        :return: A Deferred firing when the cleanup is finished.
        """


class IOperation(Interface):
    """An operation that can be performed."""

    def get_probe():
        """
        Get a probe for the operation. To ensure sequential operations
        perform real work, the operation may return a different
        probe each time.
        """


class IMetric(Interface):
    """
    A metric to be measured.
    """
    def measure(self, f, *a, **kw):
        """
        Measure the change in the metric while performing a function.

        :param f: Function to call.
        :param a: Positional arguments to function.
        :param kw: Keyword arguments to function.
        """
