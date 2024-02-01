# Submissions grouped by teams
# Submissions grouped by teams

team_alpha_submissions = [
    {"id": 1, "message": "It would be better if my manager helps improve team collaboration."},
    {"id": 2, "message": "I need more training in our new software tools to become more efficient at work."},
    {"id": 3, "message": "It would help if we have better time management strategies within the team."},
    {"id": 4, "message": "I would be more productive if I had a quieter workspace."},
    {"id": 5, "message": "Improved feedback from my manager would help me grow in my role."},
    {"id": 21, "message": "I have difficulty accessing important files and documents."},
    {"id": 22, "message": "I need better software tools for project management."},
    {"id": 23, "message": "Our team's goals and objectives are unclear, affecting our performance."},
    {"id": 24, "message": "I face issues with project prioritization and resource allocation."},
    {"id": 29, "message": "I need more opportunities for skill development and training."}
]

team_bravo_submissions = [
    {"id": 6, "message": "I often face communication issues with my team, which affects my work."},
    {"id": 7, "message": "I need more training in our new software tools to become more efficient at work."},
    {"id": 8, "message": "I find it challenging to meet tight deadlines."},
    {"id": 9, "message": "I would be more productive if I had a quieter workspace."},
    {"id": 10, "message": "Improved feedback from my manager would help me grow in my role."},
    {"id": 23, "message": "We lack a clear delegation of tasks and responsibilities."},
    {"id": 24, "message": "I require more training on using collaboration tools effectively."},
    {"id": 29, "message": "We need a better system for tracking project progress."},
    {"id": 30, "message": "Our team struggles with decision-making processes."},
    {"id": 31, "message": "Our team faces issues with task prioritization."}
]

team_charlie_submissions = [
    {"id": 11, "message": "Our team lacks clear project objectives, making it hard to focus our efforts effectively."},
    {"id": 12, "message": "I struggle with maintaining work-life balance and need support in this area to avoid burnout."},
    {"id": 13, "message": "The constant flow of meetings disrupts my workflow and makes it challenging to concentrate on tasks."},
    {"id": 14, "message": "Our communication channels are causing information to get lost and affecting our efficiency."},
    {"id": 15, "message": "I'd appreciate more training opportunities to enhance my skills and contribute effectively to the team."},
    {"id": 25, "message": "We have too many unnecessary meetings that consume our time."},
    {"id": 26, "message": "I need better access to project-related information."},
    {"id": 32, "message": "We face challenges with team collaboration and information sharing."},
    {"id": 33, "message": "Our team needs better project management tools."},
    {"id": 34, "message": "I need assistance with work prioritization."}
]

team_delta_submissions = [
    {"id": 16, "message": "Our team struggles to adapt to new technology tools, which hinders our productivity."},
    {"id": 17, "message": "I face difficulties understanding the company's long-term goals and how my work contributes to them."},
    {"id": 18, "message": "I feel isolated working remotely and miss the social interactions we had in the office."},
    {"id": 19, "message": "The lack of a dedicated feedback system makes it hard for me to provide input on the company's direction."},
    {"id": 20, "message": "More organized task management system to keep everyone on the same page and meet deadlines consistently."},
    {"id": 27, "message": "I feel disconnected from the team's decision-making process."},
    {"id": 28, "message": "I miss in-person team bonding activities and events."},
    {"id": 35, "message": "Our team needs better communication tools for remote work."},
    {"id": 36, "message": "I require more clarity on my role's contribution to the company's goals."},
    {"id": 37, "message": "I struggle with time management and task prioritization."}
]

# Team data with summarized blockers
teams = [
    {
        "id": 1,
        "name": "Team Alpha",
        "summarized_blockers": "Struggles with project prioritization, leading to delays in task completion and difficulties in meeting deadlines. This lack of clarity causes frustration and hampers overall productivity.",
        "submissions": team_alpha_submissions
    },
    {
        "id": 2,
        "name": "Team Bravo",
        "summarized_blockers": "Faces resource allocation problems, resulting in overworked team members and burnout. The lack of balanced workloads and support impacts employee morale and well-being.",
        "submissions": team_bravo_submissions
    },
    {
        "id": 3,
        "name": "Team Charlie",
        "summarized_blockers": "Deals with process inefficiencies that hinder workflow. The absence of streamlined procedures leads to wasted time and frustration, impacting the team's overall efficiency and motivation.",
        "submissions": team_charlie_submissions
    },
    {
        "id": 4,
        "name": "Team Delta",
        "summarized_blockers": "Encounters alignment issues with company goals and strategies. Team members lack clarity on the company's overarching direction, causing uncertainty and affecting their motivation and sense of purpose.",
        "submissions": team_delta_submissions
    }
]
