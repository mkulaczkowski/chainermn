Environmental Variables
=======================

``CHAINERMN_FORCE_ABORT_ON_EXCEPTIONS``
  If this variable is set to a non-emptyvlaue,
  ChainerMN installs a global hook to Python's `sys.excepthook` to call ``MPI_Abort()`` when
  an unhandled exception occurs. See :ref:`faq-global-exc-hook`
