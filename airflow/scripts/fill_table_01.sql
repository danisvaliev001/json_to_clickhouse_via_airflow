INSERT INTO uchiru.logs_raw SELECT * FROM file("/var/lib/clickhouse/user_files/raw/event-data.json", "JSONEachRow", "ts Nullable(Int8), userId Nullable(String), sessionId Nullable(Int8), page Nullable(String), auth Nullable(String), method Nullable(String), status Nullable(Int8), level Nullable(String), itemInSession Nullable(Int8), location Nullable(String), userAgent Nullable(String), lastName Nullable(String), firstName Nullable(String), registration Nullable(Int8), gender Nullable(String), artist Nullable(String), song Nullable(String), length Nullable(Float64)")