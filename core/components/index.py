from fronty import (
    html,
    css,
)

from .layout import layout


def index_page() -> html.Html:
    return layout(
        html.Div(
            html.Anchor(name="about"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div(
                                html.H1("Talk Python To Me"),
                                html.H3(
                                    "A podcast on Python and related technologies"),
                                html.Element("hr").class_("intro-divider"),
                                html.Ul(
                                    html.Li(
                                        html.Anchor(
                                            html.I().class_("fa fa fa-rss fa-fw"),
                                            html.Span(" Episodes").class_(
                                                "network-name"
                                            ),
                                            href="/episodes",
                                            title="See all episodes going back over 5 years.",
                                        ).class_("btn btn-info btn-lg"),
                                    ),
                                    html.Li(
                                        html.Anchor(
                                            html.I().class_("fa-duotone fa-mp3-player"),
                                            html.Span(" Latest").class_(
                                                "network-name"),
                                            href="/episodes/latest",
                                            title="Listen to the latest episode.",
                                        ).class_("btn btn-info btn-lg"),
                                    ),
                                    html.Li(
                                        html.Anchor(
                                            html.I().class_(
                                                "fad fa-envelope-open-text"
                                            ),
                                            html.Span(" Newsletter").class_(
                                                "network-name"
                                            ),
                                            href="/friends-of-the-show",
                                            title="Become a friend of the show. We'll send you updates on all the events.",
                                        ).class_("btn btn-info btn-lg"),
                                    ),
                                    html.Li(
                                        html.Anchor(
                                            html.I().class_("fab fa-youtube"),
                                            html.Span(" Live stream").class_(
                                                "network-name"
                                            ),
                                            href="/stream/live",
                                            title="Watch the active live stream and check in on the next scheduled event.",
                                        ).class_("btn btn-danger btn-lg"),
                                    ).class_("hidden-sm"),
                                    html.Li(
                                        html.Anchor(
                                            html.I().class_("fab fa-product-hunt"),
                                            html.Span(" Pro Edition").class_(
                                                "network-name"
                                            ),
                                            href="https://training.talkpython.fm/talk-python-pro",
                                            title="Activate Talk Python To Me [Pro Edition] without ads and full history.",
                                            target="_blank",
                                        ).class_("btn btn-success btn-lg"),
                                    ).class_("hidden-sm"),
                                ).class_("list-inline intro-social-buttons"),
                            ).class_("intro-message"),
                        ).class_("col-lg-12"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("intro-header"),
            html.Anchor().class_("latest-episode"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.H3(
                                "Latest episode:",
                                html.Break(),
                                "#448 Full-Time Open Source Devs Panel",
                            ).class_("section-heading"),
                            html.Text(
                                "So you've created a Python-based open source project and it's started to take off. You're getting contributors, lots of buzz in the podcast space, and more. But you have that day job working on Java. How do you make the transition from popular hobby project to full time job? After all, you are giving away your open source project for free, right? Well, on this episode, I have put together an amazing panel of guests who all have done exactly this: Turned their project into full time work and even companies in some cases. We have Samuel Colvin, Gina Häußge, Sebastián Ramírez, Charlie Marsh, Will McGugan and Eric Holscher on to share their stories.",
                                html.Break(),
                                html.Anchor(
                                    "Full details",
                                    href="/episodes/show/448",
                                ).class_("light-access-link"),
                                " &#187;",
                            ).class_("lead"),
                        ).class_("col-lg-5 col-sm-6"),
                        html.Div(
                            html.Div(
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/charlie-marsh.jpg?cacheId=0ceb8de7fa1140ed0df06488f11fda05",
                                        alt="Charlie Marsh",
                                        title="Charlie Marsh",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Charlie Marsh",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/gina-haussge.jpg?cacheId=8fc3c7a2566fd2cafb7948d73cd826bc",
                                        alt="Gina Häußge",
                                        title="Gina Häußge",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Gina Häußge",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/will-mcgugan.jpg?cacheId=af5b7c38c4cff9277891d6f09d7a8a51",
                                        alt="Will McGugan",
                                        title="Will McGugan",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Will McGugan",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/samuel-colvin.jpg?cacheId=d8013c326e696c06717e2593769b5c43",
                                        alt="Samuel Colvin",
                                        title="Samuel Colvin",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Samuel Colvin",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/sebastian-ramirez.jpg?cacheId=9f86973c97f1300d961af74154125891",
                                        alt="Sebastián Ramírez",
                                        title="Sebastián Ramírez",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Sebastián Ramírez",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/eric-holscher/eric-holscher.jpg?cacheId=eead68b8464cf1334fff554fc38d6f99",
                                        alt="Eric Holscher",
                                        title="Eric Holscher",
                                    ).class_("img img-circle"),
                                    html.Break(),
                                    html.Div(
                                        "Eric Holscher",
                                    ).class_("guest-name"),
                                ).class_("guest"),
                                html.Div().class_("clearfix"),
                            ).class_("guests"),
                            html.Div(
                                html.Audio(
                                    controls=True,
                                    preload="none",
                                    src="https://talkpython.fm/episodes/download/448/full-time-open-source-devs-panel.mp3",
                                ),
                                html.Break(),
                                html.Anchor(
                                    "Download MP3",
                                    target="_blank",
                                    rel="noopener",
                                    href="https://backtracks.fm/talkpython/r/talkpython.fm/episodes/download/448/448-open-source-full-time.mp3?s=1",
                                ).class_("btn btn-danger"),
                            ).class_("player"),
                            html.Div().class_("clearfix"),
                        )
                        .class_("col-lg-5 col-lg-offset-2 col-sm-6")
                        .style(
                            **{
                                "text-align": "center",
                            }
                        ),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-a latest-episode"),
            html.Anchor(name="kickstarter"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.H3(
                                "Take Python to the next level with our online courses",
                            ).style(
                                **{
                                    "margin-top": "0px",
                                }
                            ),
                            html.Div(
                                html.Anchor(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/img/courses/absolute-beginners.jpg?cacheId=139c88badc0a9551e1f73b6afe390196",
                                        title="Python for the Absolute Beginner course",
                                        alt="Course: Python for the Absolute Beginner course",
                                    ).class_("img img-responsive"),
                                    "Beginners",
                                    href="https://training.talkpython.fm/courses/explore_beginners/python-for-absolute-beginners?utm_source=talkpython",
                                ).class_("light-access-link"),
                            ).class_("course-img"),
                            html.Div(
                                html.Anchor(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/img/courses/effective-pycharm.jpg?cacheId=e38f16a23be089e533261907de50a653",
                                        title="Course: Effective PyCharm",
                                        alt="Course: Course: Effective PyCharm",
                                    ).class_("img img-responsive"),
                                    "Effective PyCharm",
                                    href="https://training.talkpython.fm/courses/explore_pycharm/mastering-pycharm-ide?utm_source=talkpython",
                                ).class_("light-access-link"),
                            ).class_("course-img"),
                            html.Div(
                                html.Anchor(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/img/courses/htmx-course.jpg?cacheId=9afa3191544458bd34ad39057328c03b",
                                        title="HTMX + Flask: Modern Python Web Apps, Hold the JavaScript",
                                        alt="Course: Python for the Absolute Beginner course",
                                    ).class_("img img-responsive"),
                                    "HMTX + Flask",
                                    href="https://training.talkpython.fm/courses/htmx-flask-modern-python-web-apps-hold-the-javascript?utm_source=talkpython",
                                ).class_("light-access-link"),
                            ).class_("course-img"),
                        ).style(
                            **{
                                "text-align": "center",
                            }
                        ),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-b kickstarter"),
            html.Anchor(name="upcoming"),
            html.Div(
                html.Div(
                    html.Div(
                        html.H3("Upcoming episodes").class_("section-heading"),
                        html.Div(
                            html.Div(
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/samuel-colvin.jpg?cacheId=d8013c326e696c06717e2593769b5c43",
                                        alt="Samuel Colvin",
                                        title="Samuel Colvin",
                                    ).class_("img img-circle"),
                                    html.Div(
                                        "Samuel Colvin",
                                        html.Div(
                                            html.Div("(up next)"),
                                        ).class_("and-then"),
                                    ).class_("name"),
                                ).class_("guest"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-3 col-md-offset-1"),
                            html.Div(
                                html.Div(
                                    html.Div(
                                        "Building UIs in Python with FastUI",
                                    )
                                    .class_("upcoming-details")
                                    .attr("episode-title", ""),
                                    html.Text().class_("episode-desc-short"),
                                ).class_("upcoming-details"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-8"),
                            html.Div().class_("clearfix"),
                        ).class_("upcoming-episode"),
                        html.Div(
                            html.Div(
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/bio_shots/stanislav-zmiev.webp?cacheId=54fe3e13da03abf139b8ec614d6e76ce",
                                        alt="Stanislav Zmiev",
                                        title="Stanislav Zmiev",
                                    ).class_("img img-circle"),
                                    html.Div(
                                        "Stanislav Zmiev",
                                        html.Div(
                                            html.Div("(and then)"),
                                        ).class_("and-then"),
                                    ).class_("name"),
                                ).class_("guest"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-3 col-md-offset-1"),
                            html.Div(
                                html.Div(
                                    html.Div(
                                        "Versioning Web APIs in Python",
                                    )
                                    .class_("upcoming-details")
                                    .attr("episode-title", ""),
                                    html.Text().class_("episode-desc-short"),
                                ).class_("upcoming-details"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-8"),
                            html.Div().class_("clearfix"),
                        ).class_("upcoming-episode"),
                        html.Div(
                            html.Div(
                                html.Div(
                                    html.Image(
                                        src="https://cdn-podcast.talkpython.fm/static/img/panel.jpg?cacheId=543f844a98322a11f0d0bab572cdabee",
                                        alt="Panelists",
                                        title="Panelists",
                                    ).class_("img img-circle"),
                                    html.Div(
                                        "Panelists",
                                        html.Div(
                                            html.Div("(and finally)"),
                                        ).class_("and-then"),
                                    ).class_("name"),
                                ).class_("guest"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-3 col-md-offset-1"),
                            html.Div(
                                html.Div(
                                    html.Div(
                                        "Djangonauts, Ready for Blast-Off",
                                    )
                                    .class_("upcoming-details")
                                    .attr("episode-title", ""),
                                    html.Text().class_("episode-desc-short"),
                                ).class_("upcoming-details"),
                                html.Div().class_("clearfix"),
                            ).class_("col-md-8"),
                            html.Div().class_("clearfix"),
                        ).class_("upcoming-episode"),
                    ).class_("row upcoming-episodes"),
                ).class_("container"),
            ).class_("content-section-a"),
            html.Anchor(name="reviews"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div().class_("col-sm-2"),
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.H3("What listeners think").class_(
                                "section-heading"),
                            html.Div(
                                html.Div(
                                    html.Blockquote(
                                        html.Div("Interesting").class_(
                                            "review-title"),
                                        "Not a how-to but addictively fascinating. It is neat to see how people are using Python.",
                                        html.Footer("JL Texaz").class_(
                                            "review-attribution"
                                        ),
                                    ).class_("review-text"),
                                ),
                                html.Div(
                                    html.Blockquote(
                                        html.Div("My favorite coding podcast").class_(
                                            "review-title"
                                        ),
                                        "Great, fun, and very informative podcast. Great guests and makes me aware of new things to check out to improve my code.",
                                        html.Footer("VPROluisteraar").class_(
                                            "review-attribution"
                                        ),
                                    ).class_("review-text"),
                                ),
                                html.Div(
                                    html.Blockquote(
                                        html.Div(
                                            "Informative, addictive, and powerful!"
                                        ).class_("review-title"),
                                        "I have been following this podcast since awhile now and I have to say that Michael does a great job picking topics which listeners relate to and all the information is very much helpful for a person who is getting their feet wet in Python or an experienced developer. Each and every episode, I learn at least one thing that motivates me to change my day to day life. I am looking for more Python stuff and I would love Michael to continue with the same speed as he is going. Highly recommended for all Pythonistas.",
                                        html.Footer("Ronak15").class_(
                                            "review-attribution"
                                        ),
                                    ).class_("review-text"),
                                ),
                            ).class_("lead"),
                            html.Div(
                                "Do you love the show and want to tell the world?",
                                html.Break(),
                                html.Anchor(
                                    "Send us a review",
                                    href="/home/contact",
                                ),
                                " or post one",
                                html.Anchor(
                                    " on iTunes",
                                    href="https://itunes.apple.com/us/podcast/talk-python-to-me-python-conversations/id979020229",
                                    target="_blank",
                                    rel="noopener",
                                ),
                                ". Thanks!",
                            ).class_("text-muted"),
                        ).class_("col-sm-8"),
                        html.Div().class_("col-sm-2"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("reviews content-section-b"),
            html.Anchor(name="pythonbytes"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.H3("Python Bytes Podcast").class_(
                                "section-heading"),
                            html.Div(
                                "Do you enjoy Talk Python To Me? We created a second podcast to be the perfect counterpart to the long-form interview format on Talk Python:",
                                html.Break(),
                                html.Break(),
                                html.Anchor(
                                    "Python Bytes:",
                                    html.Break(),
                                    "Python headlines delivered directly to your earbuds",
                                    href="https://pythonbytes.fm/",
                                    target="_blank",
                                    rel="noopener",
                                ).class_("light-access-link"),
                                html.Break(),
                                html.Break(),
                                "If you are looking for a 15 minute conversation on the topical items of the week in the Python ecosystem, be sure to jump over to",
                                html.Anchor(
                                    " Python Bytes ",
                                    href="https://pythonbytes.fm/",
                                    target="_blank",
                                    rel="noopener",
                                ).class_("light-access-link"),
                                "and subscribe.",
                            ).class_("lead"),
                        ).class_("col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6"),
                        html.Div(
                            html.Anchor(
                                html.Image(
                                    title="Python Bytes Podcast",
                                    alt="Python Bytes Podcast",
                                    src="https://cdn-podcast.talkpython.fm/static/img/python_bytes_logo_sm.jpg?cacheId=e7877e2dd5f780e4e56a6db4fd83b381",
                                )
                                .class_("img img-responsive")
                                .style(
                                    **{
                                        "border-radius": "5px",
                                    }
                                ),
                                href="https://pythonbytes.fm/",
                                target="_blank",
                                rel="noopener",
                            ),
                        ).class_("col-lg-5 col-sm-pull-6  col-sm-6"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-a"),
            html.Anchor(name="shirt"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.Div(
                                html.H3("Talk Python Merchandise").class_(
                                    "section-heading"
                                ),
                                html.Div(
                                    "Support the show and share your Python pride with the Talk Python To Me T-shirt.",
                                    html.Break(),
                                    html.Break(),
                                    html.Div(
                                        html.Anchor(
                                            "Buy shirt from Python Gear ($15)",
                                            target="_blank",
                                            rel="noopener",
                                            href="https://www.pythongear.com/products/talk-python-to-me-shirt-1?utm_source=talkpythonweb&utm_campaign=web_direct",
                                        )
                                        .class_("btn btn-success")
                                        .style(
                                            **{
                                                "color": "white",
                                                "font-size": "20px",
                                                "margin-bottom": "10px",
                                            }
                                        ),
                                    ).style(
                                        **{
                                            "text-align": "center",
                                        }
                                    ),
                                ).class_("lead"),
                            ).class_("section-heading"),
                        ).class_("col-lg-4 col-sm-5"),
                        html.Div(
                            html.Break(),
                            html.Div(
                                html.Anchor(
                                    html.Image(
                                        alt="Talk Python To Me T-Shirt",
                                        title="Talk Python To Me T-Shirt",
                                        src="https://cdn-podcast.talkpython.fm/static/img/TPTM_Shirt_Mockup.jpg?cacheId=fdd996c4156ba20753d752e39b5e4b74",
                                    ).style(
                                        **{
                                            "max-height": "225px",
                                            "border-radius": "5px",
                                            "background-color": "#777",
                                            "margin": "10px",
                                        }
                                    ),
                                    target="_blank",
                                    rel="noopener",
                                    href="https://www.pythongear.com/products/talk-python-to-me-shirt-1?utm_source=talkpythonweb&utm_campaign=web_direct",
                                ),
                            ).style(
                                **{
                                    "text-align": "center",
                                }
                            ),
                        ).class_("col-lg-6 col-lg-offset-1 col-sm-7 host-image-area"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-b"),

            html.Anchor(name="about"),
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Image(
                                src="https://cdn-podcast.talkpython.fm/static/img/michael-kennedy-2023-1k.jpg?cacheId=6ed1f540766fdb07321049f266f85a42",
                                alt="Michael Kennedy",
                                title="Your host: Michael Kennedy",
                            ).class_("img img-circle host-image"),
                            html.Break(),

                            html.Div(
                                html.Div(
                                    "Your host",
                                    html.Break(),
                                    "Michael Kennedy",
                                ).class_('host-name'),
                                html.Div(
                                    html.Anchor(
                                        html.I().class_("fa-brands fa-mastodon"),
                                        "mkennedy",
                                        href="https://fosstodon.org/@mkennedy",
                                        target="_blank",
                                        rel="noopener",
                                    ).class_("light-access-link"),
                                ).class_("hot-links"),
                            ).class_('host-image-caption'),
                        ).class_("col-lg-5 col-lg-offset-2 col-sm-6 host-image-area"),
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.H3("More about Talk Python to Me").class_(
                                "section-heading"),

                            html.Text(
                                "Talk Python to Me is a weekly podcast hosted by",
                                html.Anchor(
                                    " Michael Kennedy",
                                    target="_blank",
                                    href="https://fosstodon.org/@mkennedy",
                                ).class_("light-access-link"),
                                ". The show covers a wide array of Python topics as well as many related topics.",
                                html.Break(),
                                html.Break(),
                                "The format is a casual 1-hour conversation with industry experts.",
                                html.Break(),
                                html.Break(),
                                "Have feedback for the show? Send it to",
                                html.Anchor(
                                    " contact@talkpython.fm ",
                                    href="mailto:contact@talkpython.fm",
                                ).class_("light-access-link"),
                                ". We'd love to hear from you.",
                            ).class_("lead"),
                        ).class_("col-lg-5 col-sm-6"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-a"),

            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            html.Div().class_("clearfix"),
                            html.H3("Suggest a show or guest").class_(
                                "section-heading"),

                            html.Text(
                                "We are always on the look out for exciting topics to bring to you on Talk Python To Me. We could use your help!",
                                html.Break(),
                                html.Break(),
                                "Do you have a great idea for a show? Do know a dynamic Python personality who we should be speaking to? Send us an email!",
                                html.Break(),
                            ).class_("lead"),
                            html.Div(
                                html.Anchor(
                                    "contact@talkpython.fm",
                                    href="mailto:contact@talkpython.fm",
                                ).class_('light-access-link'),
                            ).style(**{
                                'text-align': 'center',
                                'font-size': '24px',
                            }),
                            html.Break(),
                        ).class_("col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6"),
                        html.Div(
                            html.Image(
                                src="https://cdn-podcast.talkpython.fm/static/img/suggest_guest_sm.png?cacheId=ce8394d664a98d56b84c6f8b39cfd53f",
                                title="Suggest a podcast guest",
                                alt="Suggest a podcast guest",
                            ).class_("img-responsive"),
                        ).class_("col-lg-5 col-sm-pull-6  col-sm-6"),
                    ).class_("row"),
                ).class_("container"),
            ).class_("content-section-b"),

            html.Div(
                html.Div(
                    html.Div(
                        html.Div().class_('col-lg-6'),
                        html.Div(
                            html.Div(
                                html.H3('Connect with us').class_(
                                    'connect-title'),
                            ).class_("list-inline banner-social-buttons"),

                            html.Ul(
                                html.Li(
                                    html.Anchor(
                                        html.I().class_("fa-brands fa-mastodon"),
                                        html.Span(" Mastodon").class_(
                                            "network-name"),
                                        href="https://fosstodon.org/@talkpython",
                                        target="_blank",
                                        rel="noopener",
                                    ).class_("btn btn-default btn-lg"),
                                ),
                                html.Li(
                                    html.Anchor(
                                        html.I().class_("fab fa-twitter"),
                                        html.Span(" ExTwitter").class_(
                                            "network-name"),
                                        href="https://twitter.com/talkpython",
                                        target="_blank",
                                        rel="noopener",
                                    ).class_("btn btn-default btn-lg"),
                                ),
                                html.Li(
                                    html.Anchor(
                                        html.I().class_("fa fa-envelope fa-fw"),
                                        html.Span(" Newsletter").class_(
                                            "network-name"),
                                        href="/friends-of-the-show",
                                        target="_blank",
                                        rel="noopener",
                                    ).class_("btn btn-default btn-lg"),
                                ),
                            ).class_("list-inline banner-social-buttons"),
                        ).class_('col-lg-6'),
                    ).class_('row'),
                ).class_('container'),
            ).class_('banner'),

        ).class_("home"),
    )


def not_found_page() -> html.Html:
    return layout(
        html.Div(
            html.H1("404 Page Not Found!"),
            html.Text("This pages aren't implemented yet."),
            html.Anchor(
                html.I().class_("fa fa-arrow-left"),
                " go back?",
                href="/",
            ),
        ).style(**{
            'text-align': 'center',
            'margin': '30px 0',
        }),
    )
