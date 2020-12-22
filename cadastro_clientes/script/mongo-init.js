db.createUser(
    {
        user: "cadastro",
        pwd: "1q2w3e",
        roles: [
            {
                role: "readWrite",
                db: "cadastro"
            }
        ]
    }
);