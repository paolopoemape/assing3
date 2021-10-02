import re

def count_number_pronouns(text1, text2):
    pronouns = ['I','he', 'they', 'she', 'we', 'you']
    result1 = re.findall(r"(?=\b(" + '|'.join(pronouns) + r")\b)", text1)
    result2 = re.findall(r"(?=\b(" + '|'.join(pronouns) + r")\b)", text2)
    print(len(result1))
    print(len(result2))

def count_number_modals(text1, text2):
    modals = ["can", "might", "must", "could", "should", "would", "will"]
    result1 = re.findall(r"(?=\b(" + '|'.join(modals) + r")\b)", text1)
    result2 = re.findall(r"(?=\b(" + '|'.join(modals) + r")\b)", text2)
    print(len(result1))
    print(len(result2))

def count_number_contraction(text1, text2):
    result1 = re.findall(r"\w+[`'’]\w{1,2}",text1)
    result2 = re.findall(r"\w+[`'’]\w{1,2}", text2)
    print(len(result1))
    print(len(result2))

text1 = "WASHINGTON — Pentagon leaders publicly acknowledged on Tuesday that they advised President Biden not to withdraw all troops from Afghanistan ahead of a chaotic evacuation in which 13 U.S. service members died in a suicide bombing and 10 Afghan civilians were killed in an American drone strike." \
        "During an expansive Senate hearing on the war in Afghanistan, Gen. Mark A. Milley, the chairman of the Joint Chiefs of Staff, also defended his actions in the tumultuous last months of the Trump administration, insisting that calls to his Chinese counterpart and a meeting in which he told generals to alert him if the president tried to launch a nuclear weapon were part of his duties as the country’s top military officer." \
        "General Milley was adamant that he did not go around his former boss. “My loyalty to this nation, its people, and the Constitution hasn’t changed and will never change as long as I have a breath to give,” he said. “I firmly believe in civilian control of the military as a bedrock principle essential to this republic and I am committed to ensuring the military stays clear of domestic politics.”" \
        "Some six hours of public testimony from senior Pentagon leaders were at times acrimonious and at times verging on political theater. Republican senators who had in the past defended President Donald J. Trump’s desire to withdraw American troops from Afghanistan demanded resignations from military leaders who carried out a Democratic president’s orders to withdraw. Democrats, who are traditionally tougher on military leaders, on this occasion, provided solace in the form of softer questioning and traced flaws back to the Trump administration." \
        "Under repeated questioning from Republican senators, the Pentagon leaders broke with parts of Mr. Biden’s defense of the pullout, acknowledging that they had recommended leaving 2,500 American troops on the ground, and had warned that the Afghan government and army could collapse as early as the fall if the United States withdrew its forces." \
        "General Milley called the “noncombatant evacuation” in Kabul, Afghanistan’s capital, last month “a logistical success but a strategic failure,” echoing the words of Senator Thom Tillis, Republican of North Carolina, from earlier in the hearing." \
        "Through it all, the burly and brash General Milley, the most senior military official in the country, sat before the Senate Armed Services Committee as both the protagonist and the antagonist for a narrative that changed with each senator. The other two military leaders invited to the hearing — Defense Secretary Lloyd J. Austin III and Gen. Kenneth F. McKenzie Jr., the head of the military’s Central Command — seemed almost like supporting actors at times, as the bulk of the questioning went to General Milley, who has recently been at the center of political turmoil related to revelations in several books about the Trump presidency." \
        "General Milley said that military leaders were able to give their advice to Mr. Biden in the lead-up to the president’s April decision to withdraw. Those views, the general said, had not changed since"

text2 = "In a perfect world, egos would be suppressed and inquisitive minds wouldn’t hesitate to ask questions, no matter how personal or even elementary. But at these types of things—a seminar, symposium, or something like that—when guys would prefer their conversations not be broadcast in front of their peers/competitors, and everyone’s situation is different, the one-on-ones off to the side often are the most impactful." \
        "Grant Williams gets it, since not too long ago he was in the same shoes as the 65 rookies that sat in a hotel conference room in Las Vegas this past August. So he was more than happy to set a neophyte straight after speaking on a panel about one of the most important topics the NBA’s class of 2021 must confront off the court: money." \
        "Someone said my first purchase is going to be a $100,000 car,” the Celtics forward recalls. “I’m like, ‘You know a car’s value depreciates as soon as you go off the lot.’” " \
        "There are a ton of perks when you’re good enough to play in the NBA, the most enticing being the massive amount of money to be made. Salaries for a first-year player start at $925,000 while each first-round pick from July’s draft enters the league with a guaranteed two-year contract that will earn them at least $3 million (before taxes, of course)." \
        "But not every rookie will retire in 15 years with “fuck you” money. Nor will every rookie sign ultra-lucrative third and fourth contracts or ink big endorsement deals. Sure, the average NBA player made $7.5 million last season, according to Basketball Reference. But mega earners—guys like Steph Curry, Joel Embiid, and Giannis Antetokounmpo balling on a max deal—inflate that number. The average NBA career lasts a shade under five seasons and even those that carve out a decade or more in the Association—an awesome accomplishment—will almost assuredly walk away from the game with a fraction of LeBron James’ net worth." \
        "So knowing how to properly manage your finances as a newly minted millionaire, with a finite window to maximize earnings, is really, really important. Not just to avoid being another sad story of a pro athlete that went broke, but to make that money last a lifetime and ideally create generational wealth. Balancing it all can be an anxiety-riddled exercise for the NBA’s newest players that, frankly, can’t fathom what life after basketball looks like." \
        "“Compared to everyone else, we make a tremendous amount of money,” says Bucks guard Pat Connaughton. “It’s incredible. It’s a dream. We’re fortunate, the whole nine. But I would say for the vast majority of guys in the NBA, understanding you have to make that last for 30, 40, 50, 60 more years when you’re done playing, that doesn’t always set in until it’s too late.”" \
        "Between jock taxes, state taxes, local taxes, agent fees, taking care of friends and family, and the effects behaviors now can have on your lifestyle later, it’s a lot to process. That’s precisely why the"


count_number_pronouns(text1, text2)
count_number_modals(text1, text2)
count_number_contraction(text1, text2)