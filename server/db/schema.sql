DO $$ BEGIN
    CREATE TYPE lot_state AS ENUM ('open', 'closed', 'no_data');
EXCEPTION WHEN duplicate_object THEN NULL;
END $$;

CREATE TABLE IF NOT EXISTS data (
    id BIGSERIAL PRIMARY KEY,
    lot_id TEXT NOT NULL,
    free_count INTEGER NOT NULL,
    total_count INTEGER,
    state lot_state NOT NULL,
    timestamp_downloaded TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    timestamp_source TIMESTAMP WITH TIME ZONE
);
