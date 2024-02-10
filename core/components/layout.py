from fronty import html


def navbar() -> html.Nav:
    return html.Nav(
        html.Div(
            html.Div(
                html.Button(
                    html.Span("Toggle navigation").class_("sr-only"),
                    html.Span().class_("icon-bar"),
                    html.Span().class_("icon-bar"),
                    html.Span().class_("icon-bar"),
                )
                .type("button")
                .class_("navbar-toggle")
                .attr("data-toggle", "collapse")
                .attr("data-target", "#bs-example-navbar-collapse-1"),
                html.Anchor(
                    html.Image(
                        src="https://cdn-podcast.talkpython.fm/static/img/talk_python_logo_mic.png?cache_id=dd08157a0f56a88381ec34afe167db21",
                        title="Talk Python To Me",
                        alt="Talk Python To Me",
                    ).class_("logo-image hidden-xs img img-circle"),
                    href="/",
                ).class_("navbar-brand topnav image"),
                html.Anchor(
                    html.Span("TalkPython").class_("logo-var"),
                    html.Span("[").class_("logo-operator"),
                    "'",
                    html.Span("Podcast").class_("logo-key"),
                    "'",
                    html.Span("]").class_("logo-operator"),
                    href="/",
                ).class_("navbar-brand topnav name"),
            ).class_("navbar-header"),
            html.Div(
                html.Ul(
                    html.Li(
                        html.Anchor(
                            "Episodes",
                            href="/episodes/all",
                            title="See our complete backlog of episodes going back over 5 years.",
                        )
                    ),
                    html.Li(
                        html.Anchor(
                            "Courses",
                            href="https://training.talkpython.fm/courses/all",
                            title="Take one of our world class Python courses.",
                        )
                    ),
                    html.Li(
                        html.Anchor(
                            "Live stream",
                            href="/stream/live",
                            title="Watch the video live stream of Talk Python episodes and be part of the show.",
                        )
                    ).class_("hidden-sm"),
                    html.Li(
                        html.Anchor(
                            "Guests",
                            href="/guests",
                            title="See all our guests who have appeared on the show.",
                        )
                    ).class_("hidden-sm"),
                    html.Li(
                        html.Anchor(
                            "Merch",
                            href="/home/shirt",
                            title="Get a Talk Python To Me T-Shirt.",
                        )
                    ).class_("hidden-sm"),
                    html.Li(
                        html.Anchor(
                            "Contact", href="/home/contact", title="Send us an email."
                        )
                    ),
                    html.Li(
                        html.Anchor(
                            html.I().class_("fa-duotone fa-magnifying-glass"),
                            href="/search",
                            title="Search the full text (including spoken audio) of all of our episodes.",
                        ),
                    ),
                ).class_("nav navbar-nav navbar-right"),
            )
            .class_("collapse navbar-collapse")
            .id("bs-example-navbar-collapse-1"),
        ).class_("container navbar-container"),
    ).class_("navbar navbar-default navbar-inverse navbar-fixed-top topnav")


def alert_banner() -> html.Anchor:
    return html.Anchor(
        "Learn Python with ",
        html.Span(
            "Talk Python",
        ).style(
            **{
                "color": "#fffd82",
                "font-weight": "bold",
            }
        ),
        "'s over 250 hours of courses ",
        html.I(style="color: #529AC3;").class_("fad fa-phone-laptop"),
        href="/talk-python-courses",
        id="global-sponsor-message",
        title="Learn Python with our online video courses. We have over 250 hours of the best Python courses and not a subscription in sight.",
        style="font-size: 18px;",
    )


def footer() -> html.Footer:
    return html.Footer(
        html.Div(
            html.Div().class_("col-sm-2"),
            html.Div(
                html.Div(
                    html.Anchor(
                        html.I().attr("aria-hidden", "true").class_("fa fa-headphones"),
                        " Episodes",
                        href="/episodes/all",
                        title="See our complete backlog of episodes going back over 7 years.",
                    ),
                    html.Anchor(
                        html.I().class_("fa-regular fa-people-group"),
                        " Guests",
                        href="/guests",
                        title="See all our guests who have appeared on the show",
                    ),
                    html.Anchor(
                        html.I().class_("fa-duotone fa-envelope"),
                        " Mailing list",
                        href="/friends-of-the-show",
                        title="Become a friend of the show and you won't miss an announcement.",
                    ),
                    html.Anchor(
                        html.I().class_("fad fa-phone-laptop"),
                        " Courses",
                        href="https://training.talkpython.fm/courses/all",
                        title="Take one of our world class Python courses",
                    ).class_("course-footer-link"),
                    html.Anchor(
                        html.I().class_("fa-duotone fa-magnifying-glass"),
                        " Search",
                        href="/search",
                        title="Search the full text of all of our episodes.",
                    ),
                    html.Anchor(
                        html.I().class_("fas fa-rss-square"),
                        " RSS",
                        href="/episodes/rss",
                        title="Subscribe to the podcast by direct RSS feed.",
                    )
                    .attr("data-umami-event", "Subscribe")
                    .attr("data-umami-event-platform", "RSS"),
                    html.Anchor(
                        html.I().class_("fas fa-user-secret"),
                        " Privacy",
                        href="/policies/privacy",
                    ),
                    html.Anchor(
                        html.I().class_("far fa-ad"),
                        " Our Sponsors",
                        href="/friends-of-the-show/sponsors",
                    ),
                    html.Anchor(
                        html.I().class_("far fa-ad"),
                        " Sponsor us",
                        href="/sponsor",
                        title="Sponsor the podcast and get the word out about your product or service.",
                    ),
                ).class_("footer-column first"),
            ).class_("col-sm-3"),
            html.Div(
                html.Div(
                    html.Anchor(
                        html.Div(
                            html.I().class_("fa-duotone fa-mp3-player footer-player"),
                        ).class_("icon-box"),
                        html.Span(
                            "  Subscribe",
                        ).class_("footer-title"),
                        href="/subscribe-options",
                        title="Subscribe to the podcast",
                        target="_blank",
                        rel="noopener",
                    ),
                    html.Anchor(
                        html.Div(
                            html.I().class_("fa fa-envelope fa-fw"),
                        ).class_("icon-box"),
                        html.Span(
                            " Email ",
                            html.Span("us").class_("hidden-xs hidden-sm hidden-md"),
                        ).class_("footer-title"),
                        href="mailto:contact@talkpython.fm",
                        title="Email us.",
                        target="_blank",
                        rel="noopener",
                    )
                    .attr("data-umami-event", "Contact")
                    .attr("data-umami-event-mode", "email"),
                    html.Anchor(
                        html.Div(
                            html.I().class_("fab fa-github"),
                        ).class_("icon-box"),
                        html.Span(
                            "  GitHub ",
                            html.Span("Organization").class_(
                                "hidden-xs hidden-sm hidden-md"
                            ),
                        ).class_("footer-title"),
                        href="https://github.com/,talkpython",
                        target="_blank",
                        rel="noopener",
                        title="The Talk Python GitHub organization.",
                    ),
                ).class_("footer-column social"),
            ).class_("col-sm-3"),
            html.Div(
                html.Div(
                    html.Anchor(
                        html.Div(
                            html.I().class_("fa-brands fa-mastodon"),
                        ).class_("icon-box"),
                        html.Span(
                            html.Span("  Connect on ").class_(
                                "hidden-xs hidden-sm hidden-md"
                            ),
                            "Mastodon",
                        ).class_("footer-title"),
                        href="https://fosstodon.org/@talkpython",
                        target="_blank",
                        rel="noopener",
                    )
                    .attr("data-umami-event", "Social")
                    .attr("data-umami-event-mode", "mastodon"),
                    html.Anchor(
                        html.Div(
                            html.I().class_("fab fa-youtube"),
                        ).class_("icon-box"),
                        html.Span(
                            html.Span("  Live streams on ").class_(
                                "hidden-xs hidden-sm hidden-md"
                            ),
                            "YouTube",
                        ).class_("footer-title"),
                        href="/youtube",
                        title="Catch our videos and other content we post to YouTube.",
                        target="_blank",
                        rel="noopener",
                    ).style(
                        **{
                            "white-space": "nowrap",
                        }
                    ),
                    html.Anchor(
                        html.Div(
                            html.I().class_("fa-brands fa-twitter"),
                        ).class_("icon-box"),
                        html.Span("  ExTwitter")
                        .class_("hidden-xs hidden-sm hidden-md")
                        .class_("footer-title"),
                        href="https://twitter.com/talkpython",
                        target="_blank",
                        rel="noopener",
                    )
                    .attr("data-umami-event", "Social")
                    .attr("data-umami-event-mode", "twitter"),
                ).class_("footer-column social"),
            ).class_("col-sm-3"),
        ).class_("container"),
        html.Div(
            html.Text(
                "Copyright &copy; ",
                html.Anchor(
                    "PDX Web Properties, LLC ",
                    href="https://pdxwebproperties.com/",
                ),
                "2015-2024. All Rights Reserved",
            ).class_("copyright text-muted small"),
            html.Text(
                "Made with ",
                html.I().class_("fa fa-heart"),
                " in Portland, OR, USA",
            ).class_("made-with-love text-muted small"),
        ).class_("copyright-footer"),
    )


def layout(*page_elements: html.AnyHTMLElement) -> html.Html:
    return html.Html(
        html.Head(
            html.Meta(charset="utf-8"),
            html.Meta()
            .attr("http-equiv", "X-UA-Compatible")
            .attr("content", "IE=edge"),
            html.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            html.Meta(
                name="description",
                content="Talk Python to Me is a weekly podcast hosted by developer and entrepreneur Michael Kennedy. We dive deep into the popular packages and software developers, data scientists, and incredible hobbyists doing amazing things with Python. If you're new to Python, you'll quickly learn the ins and outs of the community by hearing from the leaders. And if you've been Pythoning for years, you'll learn about your favorite packages and the hot new ones coming out of open source.",
            ),
            html.Meta(name="author", content="Michael Kennedy (@mkennedy)"),
            html.Title("Talk Python To Me Podcast"),
            html.Link(
                rel="alternate",
                type="application/rss+xml",
                title="Talk Python To Me Episodes",
                href="https://talkpython.fm/episodes/rss",
            ),
            html.Link(rel="preconnect", href="https://cdn-podcast.talkpython.fm"),
            html.Link(rel="preconnect", href="https://fonts.bunny.net"),
            html.Link(
                rel="shortcut icon",
                href="https://cdn-podcast.talkpython.fm/static/img/favicon.png?cache_id=9d4e32c70e1800a7d4b6f18084ae3aa8",
            ),
            html.Link(
                rel="apple-touch-icon",
                href="https://cdn-podcast.talkpython.fm/static/img/apple-touch/apple-touch-icon-180.png?cache_id=f05f1d4aa0b0494b126bf11439b86ef5",
            ),
            html.Link(
                rel="stylesheet",
                href="https://fonts.bunny.net/css?family=work-sans:100,100i,300,300i,400,400i,500,500i,700,700i",
            ),
            html.Link(
                rel="stylesheet",
                href="https://cdn-podcast.talkpython.fm/static/generated/css/packed.css?cache_id=401c92f0050d43cf3c9a9601fd9ef8fb",
            ),
            html.Link(
                rel="stylesheet",
                href="https://cdn-podcast.talkpython.fm/static/css/home.css?cache_id=6ed6f632456f0cf3f88841e58593045c",
            ),
            html.Script(src="https://uma.talkpython.fm/script.js")
            .attr("data-website-id", "c6c2d388-7cb2-4fa4-8d89-988cca7c01ab")
            .attr("async", ""),
        ),
        html.Body(
            navbar(),
            alert_banner(),
            *page_elements,
            footer(),
            html.Script(
                src="https://cdn-podcast.talkpython.fm/static/generated/js/packed.js?cache_id=2b85ef0d2729f4b9585b3f1de7fa2f37"
            ),
            html.Link(
                rel="stylesheet",
                href="https://cdn-podcast.talkpython.fm/static/fontawesome-pro/web-fonts-with-css/css/all.min.css?cache_id=bf2a5dfaa82bf7a17ae051d0fc06aa60",
            ),
            html.Anchor(
                "Talk Python's Mastodon",
                rel="me",
                style="display:none",
                href="https://fosstodon.org/@talkpython",
            ),
            html.Anchor(
                "Michael Kennedy's Mastodon",
                rel="me",
                style="display:none",
                href="https://fosstodon.org/@mkennedy",
            ),
        ),
    )
