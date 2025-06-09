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
