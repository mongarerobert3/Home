GET_TENANT_BY_ID = "SELECT * FROM tenants WHERE Id = ? "
DELETE_TENANT_BY_ID = "DELETE FROM tenants WHERE id = ? "
UPDATE_TENANT = "UPDATE tenants SET name = ?, email = ?, phone = ? WHERE Id = ?"