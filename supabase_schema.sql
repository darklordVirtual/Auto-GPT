-- supabase_schema.sql
-- SQL setup for running Auto-GPT with Supabase
-- This schema defines basic tables for users, sessions, tasks, memories and logs.

-- Users of the system
CREATE TABLE IF NOT EXISTS users (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    email text UNIQUE NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Sessions started by a user
CREATE TABLE IF NOT EXISTS sessions (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id uuid REFERENCES users(id) ON DELETE CASCADE,
    created_at timestamptz DEFAULT now()
);

-- Tasks created during a session
CREATE TABLE IF NOT EXISTS tasks (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id uuid REFERENCES sessions(id) ON DELETE CASCADE,
    description text NOT NULL,
    status text DEFAULT 'pending',
    created_at timestamptz DEFAULT now()
);

-- Persistent memory entries
CREATE TABLE IF NOT EXISTS memories (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id uuid REFERENCES sessions(id) ON DELETE CASCADE,
    content text NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Execution logs for auditing
CREATE TABLE IF NOT EXISTS logs (
    id bigserial PRIMARY KEY,
    session_id uuid REFERENCES sessions(id) ON DELETE CASCADE,
    message text NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Departments grouping employees
CREATE TABLE IF NOT EXISTS departments (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    name text NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Employees assigned to a department
CREATE TABLE IF NOT EXISTS employees (
    id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    department_id uuid REFERENCES departments(id) ON DELETE CASCADE,
    name text NOT NULL,
    role text NOT NULL,
    created_at timestamptz DEFAULT now()
);

-- Mapping between employees and tasks
CREATE TABLE IF NOT EXISTS employee_tasks (
    employee_id uuid REFERENCES employees(id) ON DELETE CASCADE,
    task_id uuid REFERENCES tasks(id) ON DELETE CASCADE,
    PRIMARY KEY (employee_id, task_id)
);
