# The script of the game goes in this file.

# PASSAGE NAME: Toxic

label toxic:

    $ options += 1

    "A flood of insults begins to pour from you. Every frustration you've ever had with this person is unleashed in a volley of hatred and vitriol." 

    "After two years of loving this person, you know exactly what their weak points are. They made the mistake of betraying you, the one person in the world who can target their insecurities with laser precision. You are going to WIN this." 

    "As you lay into this person, you surprise even yourself with the level of cruelty you show."

    "After several minutes of taking your verbal abuse, your ex partner just sits there. Hollow." 

    "'I deserve that,' they say, holding back tears." 

    "Damn right." 

    "They want to leave? Fine. Say something that will haunt them forever."

    menu:
        "Say the most grotesque thing you can imagine.":
            jump keep_going
        "That's enough.":
            jump stay_silent