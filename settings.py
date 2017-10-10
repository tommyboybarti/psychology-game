import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True

ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'

PAGE_FOOTER = ''

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = []

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            Source code
        </a> for the below games.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Below are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish to create your own variations.
    Click one to learn more and play.
</p>
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.01,
    'participation_fee': 1.00,
    'num_bots': 6,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'fullgame5',
        'display_name': "Full Game (Groups of 5)",
        'num_demo_participants': 5,
        'players_per_group': 5,
        'app_sequence': [
            'intro', 'toilet', 'toilet_questionnaire_1',
            'chat', 'toilet_questionnaire_2',
            'toilet2', 'toilet_questionnaire_3'
        ],
    },
    {
        'name': 'fullgame4',
        'display_name': "Full Game (Groups of 4)",
        'num_demo_participants': 4,
        'players_per_group': 4,
        'app_sequence': [
            'intro', 'toilet', 'toilet_questionnaire_1',
            'chat', 'toilet_questionnaire_2',
            'toilet2', 'toilet_questionnaire_3'
        ],
    },
    {
        'name': 'fullgame3',
        'display_name': "Full Game (Groups of 3)",
        'num_demo_participants': 3,
        'players_per_group': 3,
        'app_sequence': [
            'intro', 'toilet', 'toilet_questionnaire_1',
            'chat', 'toilet_questionnaire_2',
            'toilet2', 'toilet_questionnaire_3'
        ],
    },
]

if DEBUG:
    SESSION_CONFIGS.extend([{
            'name': 'toilet',
            'display_name': "Toilet (Group of 4)",
            'num_demo_participants': 4,
            'players_per_group': 4,
            'app_sequence': [
                'toilet2',
            ],
        },
        {
            'name': 'chat',
            'display_name': "Chat (Group of 3)",
            'num_demo_participants': 50,
            'players_per_group': 5,
            'app_sequence': [
                'chat',
            ],
        },
        {
            'name': 'questionnaire_1',
            'display_name': "Questionnaire 1",
            'num_demo_participants': 1,
            'app_sequence': [
                'toilet_questionnaire_1',
            ],
        },
        {
            'name': 'questionnaire_2',
            'display_name': "Questionnaire 2",
            'num_demo_participants': 1,
            'app_sequence': [
                'toilet_questionnaire_2',
            ],
        },
        {
            'name': 'questionnaire_3',
            'display_name': "Questionnaire 3",
            'num_demo_participants': 1,
            'app_sequence': [
                'toilet_questionnaire_3',
            ],
        }
    ])

ROOT_URLCONF = 'urls'

SENTRY_DSN = environ.get('OTREE_SENTRY')

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
