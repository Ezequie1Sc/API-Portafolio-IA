def search(self, question: str):

    question = question.lower().strip()

    candidates = []

    # ===================================================
    # PALABRAS QUE INDICAN UNA CONSULTA GENERAL
    # ===================================================

    general_project_keywords = [
        "proyecto",
        "proyectos",
        "portafolio",
        "portfolio",
        "que has hecho",
        "que haz hecho",
        "que has desarrollado",
        "que haz desarrollado",
        "has hecho",
        "haz hecho",
        "has desarrollado",
        "haz desarrollado",
        "trabajos realizados",
        "proyectos realizados",
        "proyectos personales",
        "proyectos academicos",
        "que desarrollaste",
        "que creaste",
        "que aplicaciones has hecho",
        "que aplicaciones desarrollaste",
    ]

    is_general_query = any(
        keyword in question
        for keyword in general_project_keywords
    )

    # ===================================================
    # CONSULTA GENERAL
    # ===================================================

    if is_general_query:

        # Si la pregunta menciona un proyecto específico,
        # seguimos con la búsqueda normal.
        specific_matches = []

        for item in self.index["projects"]:

            score = 0

            if item["name"].lower() in question:
                score += 10

            if item["id"].lower() in question:
                score += 10

            for keyword in item.get("keywords", []):

                if keyword.lower() in question:
                    score += 2

            if score > 0:

                specific_matches.append(
                    {
                        "file": item["file"],
                        "score": score,
                    }
                )

        # ---------------------------------------------------
        # Si encontramos proyectos específicos,
        # devolvemos esos.
        # ---------------------------------------------------

        if specific_matches:

            specific_matches.sort(
                key=lambda item: item["score"],
                reverse=True,
            )

            files = []
            used = set()

            for candidate in specific_matches:

                if candidate["file"] in used:
                    continue

                used.add(candidate["file"])
                files.append(candidate["file"])

            projects = []

            for filename in files:

                try:

                    projects.append(
                        self._load_json(filename)
                    )

                except Exception as e:

                    print(
                        f"Error cargando {filename}: {e}"
                    )

            return projects

        # ---------------------------------------------------
        # Consulta general:
        # devolver proyectos destacados
        # ---------------------------------------------------

        featured_projects = [
            item
            for item in self.index["projects"]
            if item.get("featured", False)
        ]

        projects = []

        for item in featured_projects:

            try:

                projects.append(
                    self._load_json(item["file"])
                )

            except Exception as e:

                print(
                    f"Error cargando {item['file']}: {e}"
                )

        return projects

    # ===================================================
    # CONSULTA ESPECÍFICA
    # ===================================================

    for item in self.index["projects"]:

        score = 0

        # Nombre
        if item["name"].lower() in question:
            score += 10

        # ID
        if item["id"].lower() in question:
            score += 10

        # Categoría
        if item.get("category", "").lower() in question:
            score += 3

        # Keywords
        for keyword in item.get("keywords", []):

            if keyword.lower() in question:
                score += 2

        # Proyecto destacado
        if item.get("featured", False):

            if any(
                word in question
                for word in [
                    "importante",
                    "importantes",
                    "principal",
                    "principales",
                    "mejor",
                    "mejores",
                    "destacado",
                    "destacados",
                ]
            ):
                score += 5

        if score > 0:

            candidates.append(
                {
                    "file": item["file"],
                    "score": score,
                }
            )

    # ===================================================
    # ORDENAR RESULTADOS
    # ===================================================

    candidates.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    files = []
    used = set()

    for candidate in candidates:

        if candidate["file"] in used:
            continue

        used.add(candidate["file"])
        files.append(candidate["file"])

    # ===================================================
    # CARGAR PROYECTOS
    # ===================================================

    projects = []

    for filename in files:

        try:

            projects.append(
                self._load_json(filename)
            )

        except Exception as e:

            print(
                f"Error cargando {filename}: {e}"
            )

    print(
        "\n========== PROJECT SERVICE =========="
    )
    print("Pregunta:", question)
    print("Proyectos encontrados:", len(projects))
    print("Archivos:", files)
    print("=====================================\n")

    return projects