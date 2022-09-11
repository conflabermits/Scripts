/*
-----------------------------------------------------
Wizards.com:  navigation.js
Copyright (c) 2008 Wizards of the Coast
http: //www.wizards.com/
-----------------------------------------------------
*/

Event.observe(window, 'load', function ()
{
    // For each span tag within the left nav elements (only the top level elements
    // have these span tags), watch for the click event on the span tag and stop
    // the usual click behavior. If a span is clicked, go back to element's LI tag 
    // and toggle the "active" class in order to show or hide the submenu and swap 
    // the plus/minus symbols.
    $$('#leftColumn li span').each(function (s)
    {
        var element = Element.extend(s);
        element.observe('click', respondToClick);
    });
    function respondToClick(event)
    {        
        Event.stop(event);
        var element = Event.element(event);
        var parents = element.ancestors();
        parents[0].toggleClassName('active');
    };

    // add on-off handling to the Planeswalker Points button
    $$('a.planeswalkerpoints').each(function (a)
    {
        a.observe('mouseover', function (e)
        {
            $$('a.planeswalkerpoints .static').each(function (i)
            {
                i.setStyle({ display: 'none' });
            });
            $$('a.planeswalkerpoints .active').each(function (i)
            {
                i.setStyle({ display: '' });
            });
        });
        a.observe('mouseout', function (e)
        {
            $$('a.planeswalkerpoints .static').each(function (i)
            {
                i.setStyle({ display: '' });
            });
            $$('a.planeswalkerpoints .active').each(function (i)
            {
                i.setStyle({ display: 'none' });
            });
        });
    });
});