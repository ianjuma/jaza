/****  Variables Initiation  ****/
var doc = document;
var docEl = document.documentElement;
var $body = $('body');
var $sidebar = $('.sidebar');
var $sidebarFooter = $('.sidebar .sidebar-footer');
var $mainContent = $('.main-content');
var $pageContent = $('.page-content');
var $topbar = $('.topbar');
var $logopanel = $('.logopanel');
var $sidebarWidth = $(".sidebar").width();
var content = document.querySelector('.page-content');
var is_RTL = false;
var $loader = $('#preloader');
var docHeight = $(document).height();
var windowHeight = $(window).height();
var topbarWidth = $('.topbar').width();
var headerLeftWidth = $('.header-left').width();
var headerRightWidth = $('.header-right').width();
var start = delta = end = 0;
$(window).load(function() {
    "use strict";
    setTimeout(function() {
        $('.loader-overlay').addClass('loaded');
        $('body > section').animate({
            opacity: 1,
        }, 400);
    }, 500);
});

/* ==========================================================*/
/* APPLICATION SCRIPTS                                       */
/* ========================================================= */
if ($('body').hasClass('rtl')) {
    is_RTL = true;
}

/* ==========================================================*/
/* LAYOUTS API                                                */
/* ========================================================= */
/* Create RTL: Sidebar on Right Side */
function enableRTL() {
    $('#switch-rtl').prop('checked', true);
    $('body').removeClass('rtl').addClass('rtl');
    $('html').removeClass('rtl').addClass('rtl');
    $('.sidebar').css('width', '');
    $('.sidebar .searchform input').css('width', '');
    $('.sidebar .sidebar-footer').css('width', '');
    $('.logopanel').css('width', '');
    $('.searchform input').css('width', '');
    $('.sidebar .sidebar-footer .pull-left').css('');
    $('.main-content').css('margin-left', '');
    $('.topbar').css('left', '');
    if ($('body').hasClass('sidebar-hover')) sidebarHover();
    $('#switch-rtl').prop('checked', true);
    handleboxedLayout();
    $.cookie('rtl', 1);
    $.cookie('rtl', 1, {
        path: '/'
    });
}

/* Remove RTL: Sidebar on Left Side */
function disableRTL() {
    $('#switch-rtl').prop('checked', false);
    $('html').removeClass('rtl');
    $('body').removeClass('rtl');
    $('.sidebar').css('width', '');
    $('.sidebar').css('left', '');
    $('.sidebar .searchform input').css('width', '');
    $('.sidebar .sidebar-footer').css('width', '');
    $('.logopanel').css('width', '');
    $('.searchform input').css('width', '');
    $('.sidebar .sidebar-footer .pull-left').css('');
    $('.main-content').css('margin-right', '');
    $('.topbar').css('right', '');
    if ($('body').hasClass('sidebar-hover')) sidebarHover();
    handleboxedLayout();
    $.removeCookie('rtl');
    $.removeCookie('rtl', {
        path: '/'
    });
}

/* Toggle RTL */
function toggleRTL() {
    if ($('html').hasClass('rtl')) disableRTL();
    else enableRTL();
}

/* Create Sidebar Fixed */
function handleSidebarFixed() {
    // removeSidebarHover();
    $('#switch-sidebar').prop('checked', true);
    $('#switch-submenu').prop('checked', false);
    $.removeCookie('submenu-hover');
    if ($('body').hasClass('sidebar-top')) {
        $('body').removeClass('fixed-topbar').addClass('fixed-topbar');
        $.removeCookie('fluid-topbar');
        $('#switch-topbar').prop('checked', true);
    }
    $('body').removeClass('fixed-sidebar').addClass('fixed-sidebar');
    $('.sidebar').height('');
    handleboxedLayout();
    if (!$('body').hasClass('sidebar-collapsed')) removeSubmenuHover();
    createSideScroll();
    $.removeCookie('fluid-sidebar');
    $.removeCookie('fluid-sidebar', { path: '/'});
    $.cookie('fixed-sidebar', 1);
    $.cookie('fixed-sidebar', 1, {
        path: '/'
    });
}

/* Create Sidebar Fluid / Remove Sidebar Fixed */
function handleSidebarFluid() {
    $('#switch-sidebar').prop('checked', false);
    if ($('body').hasClass('sidebar-hover')) {
        removeSidebarHover();
        $('#switch-sidebar-hover').prop('checked', false);
    }
    $('body').removeClass('fixed-sidebar');
    handleboxedLayout();
    destroySideScroll();
    $.removeCookie('fixed-sidebar');
    $.removeCookie('fixed-sidebar', {
        path: '/'
    });
    $.cookie('fluid-sidebar', 1);
    $.cookie('fluid-sidebar', 1);
    $.cookie('fluid-sidebar', 1, {
        path: '/'
    });
    $.cookie('fluid-sidebar', 1, {
        path: '/'
    });
}

/* Toggle Sidebar Fixed / Fluid */
function toggleSidebar() {
    if ($('body').hasClass('fixed-sidebar')) handleSidebarFluid();
    else handleSidebarFixed();
}


/* Create Sidebar only visible on Hover */
function createSidebarHover() {
    $('body').addClass('sidebar-hover');
    $('body').removeClass('fixed-sidebar').addClass('fixed-sidebar');
    $('.main-content').css('margin-left', '').css('margin-right', '');
    $('.topbar').css('left', '').css('right', '');
    $('body').removeClass('sidebar-top');
    removeSubmenuHover();
    removeBoxedLayout();
    removeCollapsedSidebar();
    sidebarHover();
    handleSidebarFixed();
    $('#switch-sidebar-hover').prop('checked', true);
    $('#switch-sidebar').prop('checked', true);
    $('#switch-sidebar-top').prop('checked', false);
    $('#switch-boxed').prop('checked', false);
    $.removeCookie('fluid-topbar');
    $.removeCookie('sidebar-top');
    $.removeCookie('fluid-topbar', {
        path: '/'
    });
    $.removeCookie('sidebar-top', {
        path: '/'
    });
    $.cookie('sidebar-hover', 1);
    $.cookie('sidebar-hover', 1, {
        path: '/'
    });
}

/* Remove Sidebar on Hover */
function removeSidebarHover() {
    $('#switch-sidebar-hover').prop('checked', false);
    $('body').removeClass('sidebar-hover');
    if (!$('body').hasClass('boxed')) $('.sidebar, .sidebar-footer').attr('style', '');
    $('.logopanel2').remove();
    $.removeCookie('sidebar-hover');
    $.removeCookie('sidebar-hover', {
        path: '/'
    });
}

/* Toggle Sidebar on Top */
function toggleSidebarHover() {
    if ($('body').hasClass('sidebar-hover')) removeSidebarHover();
    else createSidebarHover();
}

/* Create Sidebar Submenu visible on Hover */
function createSubmenuHover() {
    removeSidebarHover();
    removeSidebarTop();
    handleSidebarFluid();
    $('#switch-submenu-hover').prop('checked', true);
    $('body').addClass('submenu-hover');
    $('.nav-sidebar .children').css('display', '');
    $.cookie('submenu-hover', 1);
    $.cookie('submenu-hover', 1, {
        path: '/'
    });
    $('#switch-sidebar').prop('checked', false);
}

/* Remove Submenu on Hover */
function removeSubmenuHover() {
    $('#switch-submenu-hover').prop('checked', false);
    $('body').removeClass('submenu-hover');
    $('.nav-sidebar .nav-parent.active .children').css('display', 'block');
    $.removeCookie('submenu-hover');
    $.removeCookie('submenu-hover', {
        path: '/'
    });
}

/* Toggle Submenu on Hover */
function toggleSubmenuHover() {
    if ($('body').hasClass('submenu-hover')) removeSubmenuHover();
    else createSubmenuHover();
}

/* Create Topbar Fixed */
function handleTopbarFixed() {
    $('#switch-topbar').prop('checked', true);
    $('body').removeClass('fixed-topbar').addClass('fixed-topbar');
    $.removeCookie('fluid-topbar');
    $.removeCookie('fluid-topbar', {
        path: '/'
    });
}

/* Create Topbar Fluid / Remove Topbar Fixed */
function handleTopbarFluid() {
    $('#switch-topbar').prop('checked', false);
    $('body').removeClass('fixed-topbar');
    if ($('body').hasClass('sidebar-top') && $('body').hasClass('fixed-sidebar')) {
        $('body').removeClass('fixed-sidebar');
        $('#switch-sidebar').prop('checked', false);
    }
    $.cookie('fluid-topbar', 1);
    $.cookie('fluid-topbar', 1, {
        path: '/'
    });
}

/* Toggle Topbar Fixed / Fluid */
function toggleTopbar() {
    if ($('body').hasClass('fixed-topbar')) handleTopbarFluid();
    else handleTopbarFixed();
}

/* Adjust margin of content for boxed layout */
function handleboxedLayout() {
    if ($('body').hasClass('builder-admin')) return;
    $logopanel.css('left', '').css('right', '');
    $topbar.css('width', '');
    $sidebar.css('margin-left', '').css('margin-right', '');
    $sidebarFooter.css('left', '').css('right', '');
    if ($('body').hasClass('boxed')) {
        windowWidth = $(window).width();
        var container = 1200;
        var margin = (windowWidth - 1200) / 2;
        if (!$('body').hasClass('sidebar-top')) {
            if ($('body').hasClass('rtl')) {
                $logopanel.css('right', margin);
                if ($('body').hasClass('sidebar-collapsed')) {
                    $topbar.css('width', 1200);
                }
                else {
                    if ($('body').hasClass('fixed-sidebar')) {
                        $sidebar.css('margin-right', margin);
                        topbarWidth = (1200 - $sidebarWidth);
                        $('.topbar').css('width', topbarWidth);
                    }
                    $sidebarFooter.css('right', margin);
                    $topbar.css('width', 960);
                }
            }
            else {
                $logopanel.css('left', margin);
                if ($('body').hasClass('sidebar-collapsed')) {
                    $topbar.css('width', 1200);
                }
                else {
                    if ($('body').hasClass('fixed-sidebar')) {
                        $sidebar.css('margin-left', margin);
                        topbarWidth = (1200 - $sidebarWidth);
                        $('.topbar').css('width', topbarWidth);
                    }
                    $sidebarFooter.css('left', margin);
                    $topbar.css('width', 960);
                }
            }
        }
        $.backstretch(["assets/images/gallery/bg1.jpg", "assets/images/gallery/bg2.jpg", "assets/images/gallery/bg3.jpg", "assets/images/gallery/bg4.jpg"], {
            fade: 3000,
            duration: 4000
        });
    }
    if ($(window).width() < 1220) {
        removeBoxedLayout();
    }
}

/* Create Boxed Layout */
function createBoxedLayout() {
    removeSidebarHover();
    $('body').addClass('boxed');
    handleboxedLayout();
    $('#switch-boxed').prop('checked', true);
    $.cookie('boxed-layout', 1);
    $.cookie('boxed-layout', 1, {
        path: '/'
    });
}

/* Remove boxed layout */
function removeBoxedLayout() {
    if ($('body').hasClass('boxed')) {
        $('body').removeClass('boxed');
        $logopanel.css('left', '').css('right', '');
        $topbar.css('width', '');
        $sidebar.css('margin-left', '').css('margin-right', '');
        $sidebarFooter.css('left', '').css('right', '');
        $.removeCookie('boxed-layout');
        $.removeCookie('boxed-layout', {
            path: '/'
        });
        $('#switch-boxed').prop('checked', false);
        $.backstretch("destroy");
    }
}

function toggleboxedLayout() {
        if ($('body').hasClass('boxed')) removeBoxedLayout();
        else createBoxedLayout();
    }
    /* Toggle Sidebar Collapsed */
function collapsedSidebar() {
    if ($body.css('position') != 'relative') {
        if (!$body.hasClass('sidebar-collapsed')) console.log('sidebar');
    } else {
        if ($body.hasClass('sidebar-show')) $body.removeClass('sidebar-show');
        else $body.addClass('sidebar-show');
    }
    handleboxedLayout();
}

$('[data-toggle]').on('click', function(event) {
    event.preventDefault();
    var toggleLayout = $(this).data('toggle');
    if (toggleLayout == 'rtl') toggleRTL();
    if (toggleLayout == 'sidebar-behaviour') toggleSidebar();
    if (toggleLayout == 'submenu') toggleSubmenuHover();
    if (toggleLayout == 'sidebar-collapsed') collapsedSidebar();
    if (toggleLayout == 'sidebar-top') toggleSidebarTop();
    if (toggleLayout == 'sidebar-hover') toggleSidebarHover();
    if (toggleLayout == 'boxed') toggleboxedLayout();
    if (toggleLayout == 'topbar') toggleTopbar();
});

/* Reset to Default Style, remove all cookie and custom layouts */
function resetStyle() {
    $('#reset-style').on('click', function(event) {
        event.preventDefault();
        removeBoxedLayout();
        removeSidebarTop();
        removeSidebarHover();
        removeSubmenuHover();
        removeCollapsedSidebar();
        disableRTL();
        $.removeCookie('rtl');
        $.removeCookie('main-color');
        $.removeCookie('main-name');
        $.removeCookie('theme');
        $.removeCookie('bg-name');
        $.removeCookie('bg-color');
        $.removeCookie('submenu-hover');
        $.removeCookie('sidebar-collapsed');
        $.removeCookie('app-language');
        $.removeCookie('app-language', { path: '/'});
        $.removeCookie('rtl', {
            path: '/'
        });
        $.removeCookie('main-color', {
            path: '/'
        });
        $.removeCookie('main-name', {
            path: '/'
        });
        $.removeCookie('theme', {
            path: '/'
        });
        $.removeCookie('bg-name', {
            path: '/'
        });
        $.removeCookie('bg-color', {
            path: '/'
        });
        $.removeCookie('submenu-hover', {
            path: '/'
        });
        $.removeCookie('sidebar-collapsed', {
            path: '/'
        });
        $('body').removeClass(function(index, css) {
            return (css.match(/(^|\s)bg-\S+/g) || []).join(' ');
        });
        $('body').removeClass(function(index, css) {
            return (css.match(/(^|\s)color-\S+/g) || []).join(' ');
        });
        $('body').removeClass(function(index, css) {
            return (css.match(/(^|\s)theme-\S+/g) || []).join(' ');
        });
        $('body').addClass('theme-sdtl').addClass('color-default');
        $('.builder .theme-color').removeClass('active');
        $('.theme-color').each(function() {
            if ($(this).data('color') == '#319DB5') $(this).addClass('active');
        });
        $('.builder .theme').removeClass('active');
        $('.builder .theme-default').addClass('active');
        $('.builder .sp-replacer').removeClass('active');
    });
}

/**** PANEL ACTIONS ****/
function handlePanelAction() {
    /* Create Portlets Controls automatically: reload, fullscreen, toggle, remove, popout */
    function handlePanelControls() {
        $('.panel-controls').each(function() {
            var controls_html = '<div class="control-btn">' + '<a href="#" class="panel-reload hidden"><i class="icon-reload"></i></a>' + '<a class="hidden" id="dropdownMenu1" data-toggle="dropdown">' + '<i class="icon-settings"></i>' + '</a>' + '<ul class="dropdown-menu pull-right" role="menu" aria-labelledby="dropdownMenu1">' + '<li><a href="#">Action</a>' + '</li>' + '<li><a href="#">Another action</a>' + '</li>' + '<li><a href="#">Something else here</a>' + '</li>' + '</ul>' + '<a href="#" class="panel-popout hidden tt" title="Pop Out/In"><i class="icons-office-58"></i></a>' + '<a href="#" class="panel-maximize hidden"><i class="icon-size-fullscreen"></i></a>' + '<a href="#" class="panel-toggle"><i class="fa fa-angle-down"></i></a>' + '<a href="#" class="panel-close"><i class="icon-trash"></i></a>' + '</div>';
            $(this).append(controls_html);
        });
    }
    handlePanelControls();
    // Remove Panel 
    $(".panel-header .panel-close").on("click", function(event) {
        event.preventDefault();
        $item = $(this).parents(".panel:first");
        bootbox.confirm("Are you sure to remove this panel?", function(result) {
            if (result === true) {
                $item.addClass("animated bounceOutRight");
                window.setTimeout(function() {
                    $item.remove();
                }, 300);
            }
        });
    });
    // Toggle Panel Content
    $(document).on("click", ".panel-header .panel-toggle", function(event) {
        event.preventDefault();
        $(this).toggleClass("closed").parents(".panel:first").find(".panel-content").slideToggle();
    });
    // Popout / Popin Panel
    $(document).on("click", ".panel-header .panel-popout", function(event) {
        event.preventDefault();
        var panel = $(this).parents(".panel:first");
        if (panel.hasClass("modal-panel")) {
            $("i", this).removeClass("icons-office-55").addClass("icons-office-58");
            panel.removeAttr("style").removeClass("modal-panel");
            panel.find(".panel-maximize,.panel-toggle").removeClass("nevershow");
            panel.draggable("destroy").resizable("destroy");
        } else {
            panel.removeClass("maximized");
            panel.find(".panel-maximize,.panel-toggle").addClass("nevershow");
            $("i", this).removeClass("icons-office-58").addClass("icons-office-55");
            var w = panel.width();
            var h = panel.height();
            panel.addClass("modal-panel").removeAttr("style").width(w).height(h);
            $(panel).draggable({
                handle: ".panel-header",
                containment: ".page-content"
            }).css({
                "left": panel.position().left - 10,
                "top": panel.position().top + 2
            }).resizable({
                minHeight: 150,
                minWidth: 200
            });
        }
        window.setTimeout(function() {
            $("body").trigger("resize");
        }, 300);
    });
    // Reload Panel Content
    $(document).on("click", '.panel-header .panel-reload', function(event) {
        event.preventDefault();
        var el = $(this).parents(".panel:first");
        blockUI(el);
        window.setTimeout(function() {
            unblockUI(el);
        }, 1800);
    });
    // Maximize Panel Dimension 
    $(document).on("click", ".panel-header .panel-maximize", function(event) {
        event.preventDefault();
        var panel = $(this).parents(".panel:first");
        panel.removeAttr("style").toggleClass("maximized");
        if (panel.hasClass("maximized")) {
            panel.parents(".portlets:first").sortable("destroy");
            $(window).trigger('resize');
        }
        else {
            $(window).trigger('resize');
            sortablePortlets();
        }
        $("i", this).toggleClass("icon-size-fullscreen").toggleClass("icon-size-actual");
        panel.find(".panel-toggle").toggleClass("nevershow");
        $("body").trigger("resize");
        return false;
    });
}

/* ==========================================================*/
/* BEGIN SIDEBAR                                             */
/* Sidebar Sortable menu & submenu */
function handleSidebarSortable() {
    $('.menu-settings').on('click', '#reorder-menu', function(e) {
        e.preventDefault();
        $('.nav-sidebar').removeClass('remove-menu');
        $(".nav-sidebar").sortable({
            connectWith: ".nav-sidebar > li",
            handle: "a",
            placeholder: "nav-sidebar-placeholder",
            opacity: 0.5,
            axis: "y",
            dropOnEmpty: true,
            forcePlaceholderSize: true,
            receive: function(event, ui) {
                $("body").trigger("resize")
            }
        });
        /* Sortable children */
        $(".nav-sidebar .children").sortable({
            connectWith: "li",
            handle: "a",
            opacity: 0.5,
            dropOnEmpty: true,
            forcePlaceholderSize: true,
            receive: function(event, ui) {
                $("body").trigger("resize")
            }
        });
        $(this).attr("id", "end-reorder-menu");
        $(this).html('End reorder menu');
        $('.remove-menu').attr("id", "remove-menu").html('Remove menu');
    });
    /* End Sortable Menu Elements*/
    $('.menu-settings').on('click', '#end-reorder-menu', function(e) {
        e.preventDefault();
        $(".nav-sidebar").sortable();
        $(".nav-sidebar").sortable("destroy");
        $(".nav-sidebar .children").sortable().sortable("destroy");
        $(this).attr("id", "remove-menu").html('Reorder menu');
    });
}

/* Sidebar Remove Menu Elements*/
function handleSidebarRemove() {
    /* Remove Menu Elements*/
    $('.menu-settings').on('click', '#remove-menu', function(e) {
        e.preventDefault();
        $(".nav-sidebar").sortable();
        $(".nav-sidebar").sortable("destroy");
        $(".nav-sidebar .children").sortable().sortable("destroy");
        $('.nav-sidebar').removeClass('remove-menu').addClass('remove-menu');
        $(this).attr("id", "end-remove-menu").html('End remove menu');
        $('.reorder-menu').attr("id", "reorder-menu").html('Reorder menu');
    });
    /* End Remove Menu Elements*/
    $('.menu-settings').on('click', '#end-remove-menu', function(e) {
        e.preventDefault();
        $('.nav-sidebar').removeClass('remove-menu');
        $(this).attr("id", "remove-menu").html('Remove menu');
    });
    $('.sidebar').on('click', '.remove-menu > li', function() {
        $menu = $(this);
        if ($(this).hasClass('nav-parent')) $remove_txt = "Are you sure to remove this menu (all submenus will be deleted too)?";
        else $remove_txt = "Are you sure to remove this menu?";
        bootbox.confirm($remove_txt, function(result) {
            if (result === true) {
                $menu.addClass("animated bounceOutLeft");
                window.setTimeout(function() {
                    $menu.remove();
                }, 300);
            }
        });
    });
}

/* Hide User & Search Sidebar */
function handleSidebarHide() {
    hiddenElements = $(':hidden');
    visibleElements = $(':visible');
    $('.menu-settings').on('click', '#hide-top-sidebar', function(e) {
        e.preventDefault();
        var this_text = $(this).text();
        $('.sidebar .sidebar-top').slideToggle(300);
        if (this_text == 'Hide user & search') {
            $(this).text('Show user & search');
        }
    });
    $('.topbar').on('click', '.toggle-sidebar-top', function(e) {
        e.preventDefault();
        $('.sidebar .sidebar-top').slideToggle(300);
        if ($('.toggle-sidebar-top span').hasClass('icon-user-following')) {
            $('.toggle-sidebar-top span').removeClass('icon-user-following').addClass('icon-user-unfollow');
        }
        else {
            $('.toggle-sidebar-top span').removeClass('icon-user-unfollow').addClass('icon-user-following');
        }
    });
}


/* Create custom scroll for sidebar used for fixed sidebar */
function createSideScroll() {
    if ($.fn.mCustomScrollbar) {
        destroySideScroll();
        if (!$('body').hasClass('sidebar-collapsed') && !$('body').hasClass('sidebar-collapsed') && !$('body').hasClass('submenu-hover') && $('body').hasClass('fixed-sidebar')) {
            $('.sidebar-inner').mCustomScrollbar({
                scrollButtons: {
                    enable: false
                },
                autoHideScrollbar: true,
                scrollInertia: 150,
                theme: "light-thin",
                advanced: {
                    updateOnContentResize: true
                }
            });
        }
        if ($('body').hasClass('sidebar-top')) {
            destroySideScroll();
        }
    }
}

/* Destroy sidebar custom scroll */
function destroySideScroll() {
    $('.sidebar-inner').mCustomScrollbar("destroy");
}

/* Toggle submenu open */
function toggleSidebarMenu() {
    // Check if sidebar is collapsed
    if ($('body').hasClass('sidebar-collapsed') || $('body').hasClass('sidebar-top') || $('body').hasClass('submenu-hover')) $('.nav-sidebar .children').css({
        display: ''
    });
    else $('.nav-active.active .children').css('display', 'block');
    $('.sidebar').on('click', '.nav-sidebar li.nav-parent > a', function(e) {
        e.preventDefault();
        if ($('body').hasClass('sidebar-collapsed') && !$('body').hasClass('sidebar-hover')) return;
        if ($('body').hasClass('submenu-hover')) return;
        var parent = $(this).parent().parent();
        parent.children('li.active').children('.children').slideUp(200);
        $('.nav-sidebar .arrow').removeClass('active');
        parent.children('li.active').removeClass('active');
        var sub = $(this).next();
        if (sub.is(":visible")) {
            sub.children().addClass('hidden-item')
            $(this).parent().removeClass("active");
            sub.slideUp(200, function() {
                sub.children().removeClass('hidden-item')
            });
        } else {
            $(this).find('.arrow').addClass('active');
            sub.children().addClass('is-hidden');
            setTimeout(function() {
                sub.children().addClass('is-shown');
            }, 0);
            sub.slideDown(200, function() {
                $(this).parent().addClass("active");
                setTimeout(function() {
                    sub.children().removeClass('is-hidden').removeClass('is-shown');
                }, 500);
            });
        }
    });
}

// Add class everytime a mouse pointer hover over it
var hoverTimeout;
$('.nav-sidebar > li').hover(function() {
    clearTimeout(hoverTimeout);
    $(this).siblings().removeClass('nav-hover');
    $(this).addClass('nav-hover');
}, function() {
    var $self = $(this);
    hoverTimeout = setTimeout(function() {
        $self.removeClass('nav-hover');
    }, 200);
});
$('.nav-sidebar > li .children').hover(function() {
    clearTimeout(hoverTimeout);
    $(this).closest('.nav-parent').siblings().removeClass('nav-hover');
    $(this).closest('.nav-parent').addClass('nav-hover');
}, function() {
    var $self = $(this);
    hoverTimeout = setTimeout(function() {
        $(this).closest('.nav-parent').removeClass('nav-hover');
    }, 200);
});
/* END SIDEBAR                                               */
/* ========================================================= */
/* Switch Top navigation to Sidebar */
function reposition_topnav() {
    if ($('.nav-horizontal').length > 0) {
        topbarWidth = $('.topbar').width();
        headerRightWidth = $('.header-right').width();
        if ($('.header-left .nav-horizontal').length) headerLeftWidth = $('.header-left').width() + 40;
        else headerLeftWidth = $('.nav-sidebar.nav-horizontal > li').length * 140;
        var topbarSpace = topbarWidth - headerLeftWidth - headerRightWidth;
        // top navigation move to left nav if not enough space in topbar
        if ($('.nav-horizontal').css('position') == 'relative' || topbarSpace < 0) {
            if ($('.sidebar .nav-sidebar').length == 2) {
                $('.nav-horizontal').insertAfter('.nav-sidebar:eq(1)');
            } else {
                // only add to bottom if .nav-horizontal is not yet in the left panel
                if ($('.sidebar .nav-horizontal').length == 0) {
                    $('.nav-horizontal').appendTo('.sidebar-inner');
                    $('.sidebar-widgets').css('margin-bottom', 20);
                }
            }
            $('.nav-horizontal').css({
                display: 'block'
            }).addClass('nav-sidebar').css('margin-bottom', 100);
            createSideScroll();
            $('.nav-horizontal .children').removeClass('dropdown-menu');
            $('.nav-horizontal > li').each(function() {
                $(this).removeClass('open');
                $(this).find('a').removeAttr('class');
                $(this).find('a').removeAttr('data-toggle');
            });
            /* We hide mega menu in sidebar since video / images are too big and not adapted to sidebar */
            if ($('.nav-horizontal').hasClass('mmenu')) $('.nav-horizontal.mmenu').css('height', 0).css('overflow', 'hidden');
        } else {
            if ($('.sidebar .nav-horizontal').length > 0) {
                $('.sidebar-widgets').css('margin-bottom', 100);
                $('.nav-horizontal').removeClass('nav-sidebar').appendTo('.topnav');
                $('.nav-horizontal .children').addClass('dropdown-menu').removeAttr('style');
                $('.nav-horizontal li:last-child').show();
                $('.nav-horizontal > li > a').each(function() {
                    $(this).parent().removeClass('active');
                    if ($(this).parent().find('.dropdown-menu').length > 0) {
                        $(this).attr('class', 'dropdown-toggle');
                        $(this).attr('data-toggle', 'dropdown');
                    }
                });
            }
            /* If mega menu, we make it visible */
            if ($('.nav-horizontal').hasClass('mmenu')) $('.nav-horizontal.mmenu').css('height', '').css('overflow', '');
        }
    }
}

// Check if sidebar is collapsed
if ($('body').hasClass('sidebar-collapsed')) $('.nav-sidebar .children').css({
    display: ''
});
// Handles form inside of dropdown 
$('.dropdown-menu').find('form').click(function(e) {
    e.stopPropagation();
});
/***** Scroll to top button *****/
function scrollTop() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scrollup').fadeIn();
        } else {
            $('.scrollup').fadeOut();
        }
    });
    $('.scrollup').click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 1000);
        return false;
    });
}

function sidebarBehaviour() {
    windowWidth = $(window).width();
    windowHeight = $(window).height() - $('.topbar').height();
    sidebarMenuHeight = $('.nav-sidebar').height();
    if (windowWidth < 1024) {
        $('body').removeClass('sidebar-collapsed');
    }
    if ($('body').hasClass('sidebar-collapsed') && sidebarMenuHeight > windowHeight) {
        $('body').removeClass('fixed-sidebar');
        destroySideScroll();
    }
}

/* Function for datables filter in head */
function stopPropagation(evt) {
    if (evt.stopPropagation !== undefined) {
        evt.stopPropagation();
    } else {
        evt.cancelBubble = true;
    }
}

function detectIE() {
    var ua = window.navigator.userAgent;
    var msie = ua.indexOf('MSIE ');
    var trident = ua.indexOf('Trident/');
    var edge = ua.indexOf('Edge/');
    if (msie > 0 || trident > 0 || edge > 0) {
        $('html').addClass('ie-browser');   
    }
}

/****  Initiation of Main Functions  ****/
$(document).ready(function() {
    createSideScroll();
    toggleSidebarMenu();
    handleSidebarSortable();
    reposition_topnav();
    handleSidebarRemove();
    handleSidebarHide();
    handlePanelAction();
    scrollTop();
    sidebarBehaviour();
    detectIE();
    setTimeout(function() {
        handleboxedLayout();
    }, 100);

    if ($('body').hasClass('sidebar-hover')) sidebarHover();
});

/****  Resize Event Functions  ****/
$(window).resize(function() {
    setTimeout(function() {
        reposition_topnav();
        if (!$('body').hasClass('fixed-sidebar') && !$('body').hasClass('builder-admin')) sidebarBehaviour();
        handleboxedLayout();
    }, 100);
});
