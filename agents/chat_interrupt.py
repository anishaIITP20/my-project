from langgraph.types import interrupt

from state import GraphState


def chat_interrupt_node(state: GraphState):

    interrupt(
        {
            "message": "Summary generated. Ask a follow-up question or save the paper.",
            "summary": state["summary"]
        }
    )

    return {}