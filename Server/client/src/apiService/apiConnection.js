const API_URL = "http://172.20.10.2:5000"; // Update to match your Flask server IP

export const getAssistantStatus = async () => {
  try {
    const response = await fetch(`${API_URL}/api/status`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "omit",
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching assistant status:", error);
    return null;
  }
};

export const checkApiHealth = async () => {
  try {
    const response = await fetch(`${API_URL}/api/health`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "omit",
    });
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return await response.json();
  } catch (error) {
    console.error("Error checking API health:", error);
    return { status: "offline" };
  }
};
