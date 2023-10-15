from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date

class MySettings(BaseModel):
    threshold_declarative_memories: float = 0.9

@plugin
def settings_schema():   
    return MySettings.schema()

@hook
def agent_fast_reply(fast_reply, cat):
    
    n_declarative_mempries = len(cat.working_memory["declarative_memories"])
    
    if n_declarative_mempries == 0:
        fast_reply["output"]="we are off-topic, i not talk about there."
        return fast_reply
    
    return fast_reply


@hook
def before_cat_recalls_declarative_memories(config,cat):
    setting = cat.mad_hatter.plugins["mock_turtle"].load_settings()
    config["threshold"] = setting["threshold_declarative_memories"]
    return config