"""Simple classes for orchestrating multiple Auto-GPT agents as employees."""

from dataclasses import dataclass, field
from typing import List
from autogpt.cua.agent import Agent  # reuse the CUA agent as a placeholder


@dataclass
class Employee:
    """Represent an Auto-GPT powered employee with a specific role and goals."""

    name: str
    role: str
    goals: List[str] = field(default_factory=list)

    def run(self):
        """Run the employee agent with its configured goals."""
        print(f"Running employee {self.name} in role {self.role}")
        agent = Agent()
        prompts = [
            {
                "type": "message",
                "role": "system",
                "content": [{"text": f"Role: {self.role}\nGoals: {', '.join(self.goals)}"}],
            }
        ]
        agent.run_full_turn(prompts, print_steps=True)


@dataclass
class Department:
    """Collection of employees acting as a single department."""

    name: str
    employees: List[Employee] = field(default_factory=list)

    def run_all(self):
        """Run all employees in sequence."""
        print(f"Starting department: {self.name}")
        for employee in self.employees:
            employee.run()
