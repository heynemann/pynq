Introduction
------------

Microsoft created Linq (Language Integrated Query) using Expression trees, which is a math concept on how to parse operations into trees in a way that you can analyze the operations independently from the result.

Pynq is an implementation in Python of the Expression Tree theory and some of the providers. There will be more providers gradually, but Pynq will strive to make it as easy as possible to write your own provider.

TODO
----

I'm not sure yet that I'll need those,.but I think I'll probably do:

* Binary Expression for ArrayIndex_

Expressions not implemented
---------------------------

So far the following expressions aren't (and probably won't be) implemented:

* AddChecked_
* MultiplyChecked_
* SubtractChecked_
* Coalesce_ (first not null item in a list of items)
* ExclusiveOr_
* LeftShift_
* RightShift_
* Convert_
* ConvertChecked_
* UnaryPlus_
* TypeAs_

.. _AddChecked: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.addchecked.aspx
.. _MultiplyChecked: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.multiplychecked.aspx
.. _SubtractChecked: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.subtractchecked.aspx
.. _Coalesce: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.coalesce.aspx
.. _ExclusiveOr: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.exclusiveor.aspx
.. _LeftShift: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.leftshift.aspx
.. _RightShift: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.rightshift.aspx
.. _ArrayIndex: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expression.arrayindex.aspx
.. _Convert: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.convert.aspx
.. _ConvertChecked: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.convertchecked.aspx
.. _UnaryPlus: http://msdn.microsoft.com/en-us/library/bb534288.aspx
.. _TypeAs: http://msdn.microsoft.com/en-us/library/system.linq.expressions.expressiontype.typeas.aspx
