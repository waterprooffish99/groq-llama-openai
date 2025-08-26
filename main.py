from agents import Runner
from my_agent.teacher_agent import groq_agent, gemini_agent

res = Runner.run_sync(
    starting_agent = groq_agent,
    input = "Run a super beginner for loop code."
)

# print(res.final_output)

print(gemini_agent)
print(groq_agent)