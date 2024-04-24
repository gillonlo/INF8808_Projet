from dash import dcc, html


def get_page():
    return html.Div(
        [
            html.H1("Notre méthodologie"),
            html.P(
                "Dans cette page, nous allons décrire les calculs réalisés sur les données initiales pour les visualisations."
            ),
            html.H2("Visualisation n°2"),
            html.P(
                "Dans cette visualisation, nous avons tout d'abord des graphes représentant certaines statistiques d'attaque :"
            ),
            html.Div(
                [
                    html.Span(
                        "Buts marqués = Buts marqués total / nombre de matchs joués",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                    html.Br(),
                    html.Span(
                        "Passes décisives = Passes décisives total / nombre de matchs joués",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                    html.Br(),
                    html.Span(
                        "Buts hors pénalty = (Buts marqués total - Buts marqués par pénalty) / nombre de matchs joués",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                ]
            ),
            html.P(
                "Un des aspects de modification importante est la possession : pour avoir une échelle comparable visuellement, nous avons ramené le pourcentage de possession moyenne entre 2.5 et 0 (2.5 correspondant à l'équipe ayant la meilleure possession) :"
            ),
            html.Div(
                [
                    html.Span(
                        "Possession = (Possession moyenne / max(Possessions moyennes)) * 2.5",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    )
                ]
            ),
            html.P(
                "Les diagrammes sont ensuite triés de façon décroissante selon la somme des 4 critères :"
            ),
            html.Div(
                [
                    html.Span(
                        "Somme = Buts marqués + Passes décisives + Buts hors pénalty + Possession",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    )
                ]
            ),
            html.P(
                "Concernant l'aspect défensif, nous avons voulu aussi conserver le même ordre de lecture, à savoir la meilleure équipe est celle présentant le plus d'aire de diagramme. C'est pourquoi, nous avons réalisé les normalisations suivantes : "
            ),
            html.Div(
                [
                    html.Span(
                        "Buts non reçus = max(Buts reçus total / nombre de matchs joués) - (Buts reçus total / nombre de matchs joués)",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                    html.Br(),
                    html.Span(
                        "Passes adv. contrées = max(Passes décisives adv total / nombre de matchs joués) - (Passes décisives adv total / nombre de matchs joués)",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                    html.Br(),
                    html.Span(
                        "Buts hors pénalty non reçus = max(Buts reçus hors pénalty total / nombre de matchs joués) - (Buts reçus hors pénalty total / nombre de matchs joués)",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                    html.Br(),
                    html.Span(
                        "Possession = (Possession moyenne / max(Possessions moyennes)) * 2.5",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    ),
                ]
            ),
            html.P(
                "Les diagrammes sont ensuite également triés de façon décroissante selon la somme des 4 critères :"
            ),
            html.Div(
                [
                    html.Span(
                        "Somme = Buts non reçus + Passes adv. contrées + Buts hors pénalty non reçus + Possession",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    )
                ]
            ),
            html.H2("Visualisation n°3"),
            html.P(
                "Pour la troisième visualisation, deux critères ne sont pas intuitifs à comprendre et nous allons expliquer leur construction dans cette section. En premier lieu, le score associé aux joueurs correspond à la somme des critères présentés dans la séction précédente (partie attaque) :"
            ),
            html.Div(
                [
                    html.Span(
                        "Score = Buts marqués + Passes décisives + Buts hors pénalty",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    )
                ]
            ),
            html.P(
                "Ainsi, nous ne prenons en compte que les meilleurs attaquants des différentes équipes du tournoi."
            ),
            html.P(
                "Puis nous avons calculé une métrique de fatigue qui s'énonce de la manière suivante :"
            ),
            html.Div(
                [
                    html.Span(
                        "Fatigue = Minutes de jeux total / nombre de matchs joués",
                        style={"font-family": "Courier New", "margin-left": "10%"},
                    )
                ]
            ),
            html.P(
                "Cela permet ainsi de voir combien de joueur ont joué la totalité des matchs au fil de la compétition."
            ),
            html.H2("Visualisation n°4"),
            html.P(
                "Pour cette dernière visualisation, nous avons fait simplement les moyennes par région des critères mentionnés dans la visualition n°2."
            ),
            html.Div(
                dcc.Link("Retour à la visualisation", href="/"),
                style={"padding": "10px", "textAlign": "center"},
            ),
        ],
        style={"margin-left": "20%", "width": "60%"},
    )
