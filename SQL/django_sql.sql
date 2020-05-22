-- Query that will return the list of distinct values/ it must be after the
-- order_by method.
datavalues.values_list('vendor', flat=True).order_by('-vendor').distinct('vendor')

--
