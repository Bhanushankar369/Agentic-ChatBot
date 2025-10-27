from src.LangGraphAgenticAI.State.state import State

class BasicChatbotNode:
    """
    Basic chat bot login implementation
    """
    
    def __init__(self, model):
        self.llm = model
        
    def process(self, state: State) -> dict:
        """
        Represent the input state and generates a chatbot response
        """
        return {"messages": self.llm.invoke(state["messages"])}