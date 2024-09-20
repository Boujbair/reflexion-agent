from typing import List
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage, HumanMessage

from schemas import AnswerQuestion, Reflection
from chains import parser



load_dotenv()

def execute_tools(state: List[BaseMessage]) -> List[ToolMessage]:
    tool_invocation: AIMessage = state[-1]
    parsed_tool_calls = parser.invoke(tool_invocation)


if __name__ == "__main__":
    print("Tool Executor Enter")

    human_message = HumanMessage(
        content = "Write about AI-Powered SOC / autonomous soc problem domain,"
        "list startups that do that and raised capital."
    )

    answer = AnswerQuestion(
        answer="",
        reflection=Reflection(missing="", superfluous=""),
        search_queries=[
            "AI-powered SOC startups funding",
            "AI SOC problem domain specifics",
            "Technologies used by AI-powered SOC startups",
        ],
        id="**************"
    )

    raw_res = execute_tools(
        state=[
            human_message,
            AIMessage(
                content="",
                tool_calls=[
                    {
                        "name": AnswerQuestion.__name__,
                        "args": answer.dict(),
                        "id": "****************",
                    }
                ],
            ),
        ]
    )