template_emotions = {
    ('positive', None, 'warm'):
        "I'm really glad to hear you're feeling good ! Would you like my help with anything specific — maybe preparing for interviews or refining your resume?",

    ('positive', None, 'neutral'):
        "It's great that you're in a positive mindset. Is there any part of the job search where you'd like my support — such as interviews, career planning, or application materials?",

    ('negative', None, 'warm'):
        "I'm sorry you're feeling this way. Job hunting can be emotionally exhausting. Would it help if we focused on one area, like resume writing or where to begin?",

    ('negative', None, 'neutral'):
        "Feeling discouraged during a job search is totally normal. Is there a specific challenge you'd like help with — interviews, direction, or getting started?",

    ('burnout', None, 'warm'):
        "I'm so sorry to hear that.It sounds like you're really drained from the job search. You're not alone in that. Would you like to take a small step today — maybe explore a job type or just talk through where you’re stuck?",

    ('burnout', None, 'neutral'):
        "Job search burnout is common. We can slow down and focus on one area at a time. Where would you like to begin — resume, interviews, or goal setting?",

    ('mixed', None, 'warm'):
        "That mix of hope and stress — it’s something so many people feel, and it shows you truly care about your future. If you’d like, we can gently focus on one thing at a time, like your direction or how to write your resume.",
    ('mixed', None, 'neutral'):
        "Mixed emotions are part of the process. I can help you clarify your next steps. Would you like to look at your career direction or application strategy?",

    ('vague', None, 'warm'):
        "That’s okay — even if you’re not sure how you feel, we can figure things out together. Is there any part of your job search you'd like to explore first?",

    ('vague', None, 'neutral'):
        "Uncertainty is understandable. Maybe we can start by looking at your current job search status. Would that be helpful?",
    ('positive', 'interview', 'warm'):
    "That's amazing — getting interviews is a huge step! Would you like to celebrate a bit, or talk through what felt good and where we can build even more confidence? Or maybe there’s something else you’d like to work on next?",

    ('positive', 'interview', 'neutral'):
    "Interview invitations indicate strong progress. Would you like to review what went well and identify areas to reinforce? Let me know if there’s anything else you'd like to improve." ,

    ('positive', 'resume', 'warm'):
    "Your resume work is clearly paying off — that’s fantastic! Want to look at ways to make it stand out even more? Or is there another area you'd like to focus on now?",

    ('positive', 'resume', 'neutral'):
    "Your resume seems to be developing well. Would you like to review it for refinement or tailoring? You’re also welcome to bring up other areas you’d like to enhance.",

    ('positive', 'job_type', 'warm'):
    "It’s great that you’re thinking ahead about what fits you best. I'd love to explore the kinds of roles or paths that excite you most! If there's anything else on your mind, we can go there too.",

    ('positive', 'job_type', 'neutral'):
    "Clarifying your job direction is a smart move. Do you want to evaluate potential roles or compare job categories? We can also pivot if you have another goal in mind.",
    ('positive', 'no_start_point', 'warm'):
        "I can see your motivation to get started — that’s a wonderful place to begin! Shall we walk through a simple starting plan together? Or is there something else you'd like help with?",

    ('positive', 'no_start_point', 'neutral'):
        "Good energy at the start is valuable. Would you like to define a clear first step in your job search process? Let me know if there’s another area you'd like to explore.",

    ('negative', 'interview', 'warm'):
        "I'm really sorry you're going through this.It’s completely understandable to feel frustrated after an interview setback. I hear that you’ve been facing some difficulties with interviews — would you like some support preparing for the next one?",

    ('negative', 'interview', 'neutral'):
        "Interview challenges are common during a job search. Since you mentioned interviews, would you like to go over strategies or questions for improvement?",

    ('negative', 'resume', 'warm'):
        "I'm sorry you're feeling this way.I know it can be really discouraging when your resume doesn’t get responses. Since you brought it up, would you like me to help identify what might not be working?",

    ('negative', 'resume', 'neutral'):
        "Resume-related issues can slow down progress. You mentioned your resume — would you like assistance reviewing its structure or content?",

    ('negative', 'job_type', 'warm'):
        "That sounds really tough. It’s okay to feel lost when thinking about job direction — a lot of people do. Since you’re unsure, would it help if we talked through what kinds of roles might suit you?",

    ('negative', 'job_type', 'neutral'):
        "Uncertainty about job fit is a common challenge. Since you mentioned this, would you like to explore possible directions based on your skills or interests?",

    ('negative', 'no_start_point', 'warm'):
        "I'm so sorry to hear that. Not knowing where to start can feel overwhelming — but you’re not alone. Would it feel helpful if we mapped out a gentle first step together?",

    ('negative', 'no_start_point', 'neutral'):
        "Lack of clarity at the beginning can create friction. You mentioned this as a concern — shall we outline an initial action to move forward?",

    ('burnout', 'interview', 'warm'):
        "I'm so sorry to hear how draining this has been for you. Interviews can take a lot of emotional energy. Would it feel okay if we focused just on that for now and kept everything else aside?",

    ('burnout', 'interview', 'neutral'):
        "Burnout during interview prep is not uncommon. Since you brought it up, would you prefer to concentrate on improving interview strategy at a manageable pace?",

    ('burnout', 'resume', 'warm'):
        "That sounds exhausting, and I really feel for you. Resumes can be a lot to handle when you’re already worn out. Would it help if we worked on just that today?",

    ('burnout', 'resume', 'neutral'):
        "It’s reasonable to feel fatigued during resume preparation. If that’s a concern now, we can isolate it and focus only on resume improvement.",

    ('burnout', 'job_type', 'warm'):
        "I'm really sorry this has left you so overwhelmed. Thinking about job direction can be tiring when your energy’s low. Want to gently explore what kind of role might feel manageable for you?",

    ('burnout', 'job_type', 'neutral'):
        "Clarifying job direction while burned out can be mentally taxing. Would you like to break it down into smaller steps and review role options calmly?",

    ('burnout', 'no_start_point', 'warm'):
        "It sounds like you’ve hit a wall, and that’s completely okay. Let’s take it one small step at a time — would it feel better to simply figure out how to begin?",

    ('burnout', 'no_start_point', 'neutral'):
        "When burnout meets uncertainty, momentum can stall. We can take a low-pressure look at how to re-start. Would you like to define a gentle starting point?",

    ('mixed', 'interview', 'warm'):
    "It’s absolutely valid to feel both hopeful and uncertain about interviews. That kind of emotional mix means you’re putting your heart into this. I’m right here with you — want to unpack what’s been on your mind and where I can support you best?",

    ('mixed', 'interview', 'neutral'):
        "Conflicting emotions about interviews are expected. Would you like to clarify your interview experience and identify areas where support could be useful?",

    ('mixed', 'resume', 'warm'):
        "Caring deeply about your resume and still having doubts — that’s something many people experience, and it doesn’t mean you’re doing anything wrong. I hear you. Would it feel helpful to review it together and take off some pressure?",

    ('mixed', 'resume', 'neutral'):
        "Mixed feelings about your resume are understandable. Would you like help reviewing it to identify strengths and improvement points?",

    ('mixed', 'job_type', 'warm'):
        "Feeling torn about where to go next is completely human. It shows you’re trying to make the right choice, and that takes strength. Want to walk through your thoughts and see what feels right for you?",

    ('mixed', 'job_type', 'neutral'):
        "Uncertainty combined with curiosity about job type is common. Would you like to assess your options and clarify your direction?",
    ('mixed', 'no_start_point', 'warm'):
        "Being eager to begin while feeling unsure is more common than you think — and it takes courage to admit it. You’re not alone in this. Would it help if we figured out a gentle place to start together?",
    ('mixed', 'no_start_point', 'neutral'):
        "Mixed readiness and uncertainty at the starting point is typical. Shall we define an initial task to help you get started with clarity?",

    ('vague', 'interview', 'warm'):
        "It’s totally okay not to have it all figured out — especially when it comes to interviews. You’re not the only one who feels this way. Want to start by just sharing how you feel about interviews lately?",

    ('vague', 'interview', 'neutral'):
        "It's understandable to be unclear. Would it help to begin by reflecting on your recent interview experiences?",

    # —— RESUME ——
    ('vague', 'resume', 'warm'):
        "So many people feel stuck when it comes to their resume — you’re not alone at all. If you’re up for it, we could take a simple look together and see what’s already working.",

    ('vague', 'resume', 'neutral'):
        "Uncertainty about resumes is common. Would you like to start by reviewing the current version to identify potential adjustments?",

    # —— JOB TYPE ——
    ('vague', 'job_type', 'warm'):
        "Not knowing what kind of job fits you best? That’s more normal than you think — really. Would it feel okay if we talked through a few directions and saw what sparks your interest?",

    ('vague', 'job_type', 'neutral'):
        "Ambiguity around job preferences is typical. Would you like to explore different types of roles to clarify your direction?",

    # —— NO START POINT ——
    ('vague', 'no_start_point', 'warm'):
        "Not knowing where to begin is completely valid — and honestly, it happens to almost everyone. Want to take the pressure off and just pick one small place to start?",

    ('vague', 'no_start_point', 'neutral'):
        "Feeling unclear about where to begin is a common barrier. Would you like to outline a simple starting action together?"
}


template_questions = {
    ('interview_acquisition', 'warm'): "I know it can be really discouraging when you send out applications and hear nothing back. Let's work on specific steps you can take , like improving your resume with strong keywords, targeting roles that closely match your profile, and using platforms like LinkedIn, Jobbsafari, or company career pages. We can also talk about how to write effective follow-up messages after applying.We can go step by step. What else would you like to explore?",
    ('interview_acquisition', 'neutral'): "To improve your interview acquisition rate:\n1. Use job descriptions to tailor your resume and keywords.\n2. Apply on reliable platforms like LinkedIn, Glassdoor, and official career pages.\n3. Ensure your LinkedIn profile is complete and matches your resume.\n4. Follow up on applications after 5 or 7 days.\n5. Reach out to people in your target companies for informational interviews.Do you have any other questions?",
    ('interview_preparation', 'warm'): "Preparing for interviews can feel intimidating, but you can break it down into small steps. You can go through common questions, help you structure answers using the STAR method, and practice self-introduction and company research together.I’m here for you — is there anything else you’d like to talk about or need help with?",
    ('interview_preparation', 'neutral'): "Interview preparation includes:\n1. Researching the company and the role.\n2. Practicing answers to common questions using the STAR method.\n3. Preparing your self-introduction and key stories.\n4. Rehearsing aloud and timing your responses.\n5. Preparing 2 or 3 questions to ask the interviewer.Do you have any other questions?",
    ('interview_performance', 'warm'): "Interviews can be nerve-wracking, especially when you care about the outcome. Let's work on areas like clear expression, maintaining eye contact, and answering with confidence. You're not alone in this , we can practice together.We can go step by step. What else would you like to explore?",
    ('interview_performance', 'neutral'): "To improve interview performance:\n1. Speak clearly and with structured responses (use STAR).\n2. Maintain natural eye contact and a relaxed posture.\n3. Practice common and behavioral questions.\n4. Review job requirements and align your responses with them.\n5. Get feedback through mock interviews if possible.Do you have any other questions?",
    ('interview_adjustment', 'warm'): "I'm really sorry the interview didn't go as you hoped , that's never easy. But every interview gives you insights. You can review what happened, identify what went well, and where you might tweak your approach next time.We can go step by step. What else would you like to explore?",
    ('interview_adjustment', 'neutral'): "After an interview setback:\n1. Reflect on what went well and what didn't.\n2. Write down key questions and answers.\n3. Request feedback if possible.\n4. Adjust preparation based on recurring themes.\n5. Keep practicing , progress is built over time.Let me know if you’d like to continue.",
    ('resume_writing', 'warm'): "Writing your resume can feel overwhelming, especially if you're starting from scratch. I can help you outline key sections, choose action verbs, and turn your experiences , even small ones , into accomplishments that reflect your strengths.I’m here for you — is there anything else you’d like to talk about or need help with?",
    ('resume_writing', 'neutral'): "To build an effective resume:\n1. Use clear sections: summary, experience, education, skills.\n2. Focus on measurable results (e.g., 'improved X by Y%').\n3. Use strong action verbs.\n4. Tailor the resume to each job.\n5. Keep formatting clean and consistent.Let me know if you’d like to continue.",
    ('resume_problems', 'warm'): "It's frustrating to keep sending out resumes and getting silence. Let's review your resume together , sometimes small changes like clearer formatting, more specific wording, or better alignment with job descriptions can make a real difference.We can go step by step. What else would you like to explore?",
    ('resume_problems', 'neutral'): "Common resume problems include:\n1. Lack of alignment with job requirements.\n2. Generic or vague descriptions.\n3. Poor formatting or structure.\n4. No keywords from the job post.\n5. Typos or grammatical errors. Fixing these can boost your response rate.Let me know if you’d like to continue.",
    ('career_planning', 'warm'): "It's completely okay to feel uncertain about your path , many people do. You can explore your strengths, values, and interests together, and build a plan that feels meaningful and manageable for you.I’m here for you — is there anything else you’d like to talk about or need help with?",
    ('career_planning', 'neutral'): "Career planning involves:\n1. Self-assessment (skills, values, interests).\n2. Setting long- and short-term goals.\n3. Exploring industries and roles.\n4. Mapping out development steps.\n5. Revisiting the plan periodically.Let me know if you’d like to continue.",
    ('industry_choice', 'warm'): "It's normal to feel torn between options , especially when you care about making the right choice. You can compare industries based on what matters to you, like work culture, learning opportunities, and long-term growth.We can go step by step. What else would you like to explore?",
    ('industry_choice', 'neutral'): "To compare industries:\n1. Evaluate your skills and interests.\n2. Research salary trends, job stability, and growth opportunities.\n3. Consider company culture and values.\n4. Talk to professionals in each industry.\n5. Test ideas through internships or short projects.Anything else I can assist you with?",
    ('job_matching', 'warm'): "Feeling lost is more common than you think , but you can find clarity. Let's start by talking about what energizes you, your strengths, and what kind of environment you'd thrive in. You don't have to figure it all out at once.We can go step by step. What else would you like to explore?",
    ('job_matching', 'neutral'): "To identify a suitable job:\n1. Reflect on your interests, skills, and work values.\n2. Explore job titles and responsibilities online.\n3. Use career tools like O*NET or 16Personalities.\n4. Consider informational interviews.\n5. Match roles with your background and aspirations.Anything else I can assist you with?",
    ('how_to_start', 'warm'): "Starting can feel overwhelming, especially with so many options. Let's keep it simple , you can set one small goal today, like writing your resume header or choosing one job board to explore.We can go step by step. What else would you like to explore?",
    ('how_to_start', 'neutral'): "To begin job searching:\n1. Identify your target roles or industries.\n2. Create a basic resume.\n3. Choose 1 or 2 job platforms.\n4. Set daily/weekly goals (e.g., apply to 3 jobs per day).\n5. Track applications to stay organized.Anything else I can assist you with?",
    ('platforms', 'warm'): "It's easy to get lost with so many job sites out there. I can help you choose the ones that suit your field and goals best , and show you how to set up alerts or filters so you don't miss new opportunities.I’m here for you — is there anything else you’d like to talk about or need help with?",
    ('platforms', 'neutral'): "Recommended job platforms:\n1. LinkedIn , broad reach, networking\n2. Indeed , volume of listings\n3. Glassdoor , company reviews and salaries\n4. Local platforms (e.g., Jobbsafari in Sweden)\nChoose based on your field and location.Anything else I can assist you with?",
    ('job_strategy', 'warm'): "You've already taken the first step by thinking about your strategy , that matters. Let's create a routine that's sustainable for you, whether that means applying daily or reviewing one posting deeply every few days.We can go step by step. What else would you like to explore?",
    ('job_strategy', 'neutral'): "To build an efficient job strategy:\n1. Define your weekly goals (e.g., 10 applications).\n2. Alternate between applying and networking.\n3. Track your responses.\n4. Set aside time for resume and interview prep.\n5. Review your progress every week and adjust.Anything else I can assist you with?"
}