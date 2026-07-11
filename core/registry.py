class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool):
        self.tools[tool.name] = tool
    
    def get_tools(self, name):
        return self.tools.get(name)

    def all_tools(self):
        return self.tools.values()
    
