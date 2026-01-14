#!/usr/bin/env python3
"""
Cloud Agent Delegation Demo
This module demonstrates the concept of delegating tasks to a cloud agent.
"""


class CloudAgent:
    """A simple cloud agent that can process delegated tasks."""
    
    def __init__(self, name="CloudAgent"):
        self.name = name
        self.approved_changes = []
    
    def approve_change(self, change_description):
        """
        Approve a change and add it to the approved changes list.
        
        Args:
            change_description (str): Description of the change to approve
        
        Returns:
            bool: True if change was approved successfully
        """
        if change_description and isinstance(change_description, str) and change_description.strip():
            self.approved_changes.append(change_description)
            print(f"✓ {self.name}: 變更已認可 (Change approved) - {change_description}")
            return True
        return False
    
    def delegate_task(self, task_description):
        """
        Delegate a task to the cloud agent for processing.
        
        Args:
            task_description (str): Description of the task to delegate
        
        Returns:
            dict: Result of the delegation, or None if task is invalid
        """
        if not task_description or not isinstance(task_description, str) or not task_description.strip():
            return None
        
        result = {
            "status": "delegated",
            "task": task_description,
            "agent": self.name,
            "message": f"任務已委派至雲端代理程式 (Task delegated to cloud agent)"
        }
        print(f"→ {self.name}: {result['message']} - {task_description}")
        return result
    
    def get_approved_changes(self):
        """
        Get list of all approved changes.
        
        Returns:
            list: List of approved changes
        """
        return self.approved_changes


def main():
    """Main function demonstrating cloud agent usage."""
    print("=== 雲端代理程式示範 (Cloud Agent Demo) ===\n")
    
    # Create a cloud agent instance
    agent = CloudAgent("雲端助手")
    
    # Approve some changes
    agent.approve_change("更新配置文件 (Update configuration file)")
    agent.approve_change("修復安全漏洞 (Fix security vulnerability)")
    
    # Delegate tasks
    agent.delegate_task("部署新版本 (Deploy new version)")
    agent.delegate_task("執行自動化測試 (Run automated tests)")
    
    # Show approved changes
    print(f"\n已認可的變更 (Approved changes): {len(agent.get_approved_changes())}")
    for i, change in enumerate(agent.get_approved_changes(), 1):
        print(f"  {i}. {change}")


if __name__ == "__main__":
    main()
