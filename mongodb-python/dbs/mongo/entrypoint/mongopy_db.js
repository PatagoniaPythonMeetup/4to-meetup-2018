db.createUser(
  {
    user: 'mongopy',
    pwd: 'm0ng0py',
    roles: [ { role: 'readWrite', db: 'mongopy_db' } ]
  }
);
