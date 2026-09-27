-- ==============================================================================
-- MIGRACIÓN SUPABASE: ESQUEMA AISLADO com_control61 (BY TONI)
-- ==============================================================================

CREATE SCHEMA IF NOT EXISTS com_control61;
GRANT USAGE ON SCHEMA com_control61 TO anon, authenticated, service_role, authenticator;
GRANT ALL ON ALL TABLES IN SCHEMA com_control61 TO anon, authenticated, service_role, authenticator;
GRANT ALL ON ALL SEQUENCES IN SCHEMA com_control61 TO anon, authenticated, service_role, authenticator;
ALTER DEFAULT PRIVILEGES IN SCHEMA com_control61 GRANT ALL ON TABLES TO anon, authenticated, service_role, authenticator;

CREATE TABLE IF NOT EXISTS com_control61.devices (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  ip_address TEXT,
  status TEXT DEFAULT 'online',
  telemetry JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

ALTER TABLE com_control61.devices ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS "Allow all for devices" ON com_control61.devices;
CREATE POLICY "Allow all for devices" ON com_control61.devices FOR ALL USING (true) WITH CHECK (true);
