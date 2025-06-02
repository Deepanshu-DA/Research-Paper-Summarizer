from langgraph.graph import StateGraph, END
from agents.planner import TaskPlanner
from agents.collector import DataCollector
from agents.verifier import SourceVerifier
from agents.summarizer import Summarizer
from agents.reporter import ReportGenerator

planner = TaskPlanner()
collector = DataCollector()
verifier = SourceVerifier()
summarizer = Summarizer()
reporter = ReportGenerator()

def plan_step(state):
    query = state["query"]
    return {"tasks": planner.plan(query)}

def collect_step(state):
    tasks = state["tasks"]
    NEWS_API_KEY = "YOUR_NEWS_API"
    return {"raw_data": collector.collect(tasks, NEWS_API_KEY)}

def verify_step(state):
    raw = state["raw_data"]
    return {"verified_data": verifier.verify(raw)}

def summarize_step(state):
    verified = state["verified_data"]
    return {"summary": summarizer.summarize(verified)}

def write_step(state):
    summary = state["summary"]
    return {"report": reporter.generate(summary)}

# ✅ Define the state type
graph = StateGraph(dict)

# Add nodes
graph.add_node("planner", plan_step)
graph.add_node("collector", collect_step)
graph.add_node("verify", verify_step)
graph.add_node("summarize", summarize_step)
graph.add_node("write", write_step)

# Define flow
graph.set_entry_point("planner")
graph.add_edge("planner", "collector")
graph.add_edge("collector", "verify")
graph.add_edge("verify", "summarize")
graph.add_edge("summarize", "write")
graph.add_edge("write", END)

# ✅ Compile the graph
graph = graph.compile()
