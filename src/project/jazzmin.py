

URL="http://192.168.100.41:8000"





































JAZZMIN_SETTINGS = {
    "site_title": "Printing_CRM",
    "site_header": "Printing_CRM",
    "site_brand": "Printing_CRM",
    "site_icon": "./en/img/logo_icon.png",
    # Add your own branding here
    "site_logo": "./en/img/logo_icon.png",
    "welcome_sign": "Welcome to the Printing_CRM",
    # Copyright on the footer

    # Welcome text on the login screen
    "welcome_sign": "WELCOME HOME,",

    # Copyright on the footer
    "copyright": "Abdulrahman_Elsharef",

    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    # "search_model": ["Customer.phone_1", "Order.OrderId"],

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "Abdulrahman Elsharef",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        # {"name": "Support", "url": "https://github.com/AbdulrahmanElsharef",
        #     "new_window": True},

        # model admin to link to (Permissions checked against model)
        # {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "Dr_Print"},{"app": "Etbaly_Shokran"},{"app": "Melouk_Eltibah"},{"app": "Print_Square"},{"app": "New_Project_1"},{"app": "New_Project_2"},
        
        {"name": "Dashboard", 
         "url": f"{URL}/Dashboard",
            "new_window": True,
            "icon": "fas fa-tachometer",},
        # {"name": "Printing", "url": f"{URL}/Print_list",
        #     "new_window": True},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support" , "url": "https://github.com/AbdulrahmanElsharef","new_window": True},
        {"model": "auth.user"} ,
        # {"name": "orders", "url": "http://10.0.0.21:8000/orders","new_window": True},
        ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ["New_Project_1","New_Project_2"],

    # Hide these models when generating side menu (e.g auth.user)
    # "hide_models": ["newsales.Order"],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth","CRM_Data.City","Dr_Print.Dr_Print_Order","Etbaly_Shokran.Etbaly_Shokran_Order","Melouk_Eltibah.Melouk_Eltibah_Order","Print_Square.Print_Square_Order"],


    # Custom links to append to app groups, keyed on app name

    # "custom_links": {
    #     "Dr_Print.Order": [{
    #         "name": "Print",
    #         "url": "http://192.168.1.3:8000/newsales/Orders_Data",
    #         "new_window": True,
    #         "icon": "fas fa-tachometer",}],
    # },
    # fa-tachometer

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "bi bi-arrow-bar-right",
    "default_icon_children": "fa fa-arrow-right",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": False,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "carousel",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "vertical_tabs", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
}
