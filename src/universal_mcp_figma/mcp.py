
from universal_mcp.servers.server import SingleMCPServer
from universal_mcp.integrations.agentr import AgentRIntegration
from universal_mcp.stores.store import EnvironmentStore

from universal_mcp_figma.app import FigmaApp

env_store = EnvironmentStore()
integration_instance = AgentRIntegration(name="figma", store=env_store)
app_instance = FigmaApp(integration=integration_instance)

mcp = SingleMCPServer(
    app_instance=app_instance,
)

if __name__ == "__main__":
    mcp.run()


