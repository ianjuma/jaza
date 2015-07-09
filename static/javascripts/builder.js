/**** BUILDER FUNCTIONS ****/
function toggleBuilder() {
    $('.builder-toggle').on('click', function(){
        if($('#builder').hasClass('open')) $('#builder').removeClass('open');
        else $('#builder').addClass('open');
    });
}

/* Active Custom Scroll for Builder Sidebar */
function builderScroll() {
    $('.builder .inner').mCustomScrollbar("destroy");
    scroll_height = "100%";
    $('.builder .inner').mCustomScrollbar({
        scrollButtons: {
            enable: false
        },
        autoHideScrollbar: true,
        scrollInertia: 150,
        theme: "light",
        set_height: scroll_height,
        advanced: {
            updateOnContentResize: true
        }
    });
}

/* Enable / Disable Layouts */
function handleLayout() {
    $('.layout-option input').on('click', function(){
        var layout = $(this).attr('data-layout');
        var is_checked = $(this).prop('checked');
        if(layout == 'rtl' && is_checked == true) toggleRTL();
        if(layout == 'rtl' && is_checked == false) toggleRTL();
        if(layout == 'sidebar' && is_checked == true) handleSidebarFixed();
        if(layout == 'sidebar' && is_checked == false) handleSidebarFluid();
        if(layout == 'topbar' && is_checked == true) handleTopbarFixed();
        if(layout == 'topbar' && is_checked == false) handleTopbarFluid();
        if(layout == 'sidebar-hover' && is_checked == true) createSidebarHover();
        if(layout == 'sidebar-hover' && is_checked == false) removeSidebarHover();
        if(layout == 'submenu-hover' && is_checked == true) createSubmenuHover();
        if(layout == 'submenu-hover' && is_checked == false) removeSubmenuHover();
        if(layout == 'sidebar-top' && is_checked == true) createSidebarTop();
        if(layout == 'sidebar-top' && is_checked == false) removeSidebarTop();
        if(layout == 'boxed' && is_checked == true) createBoxedLayout();
        if(layout == 'boxed' && is_checked == false) removeBoxedLayout();
    });
}

$(document).ready(function() {
   "use strict";

    toggleBuilder();
    builderScroll();
    handleLayout();

    if($('body').hasClass('sidebar-top')){
      destroySideScroll();
    }

});
