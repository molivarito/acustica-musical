-- Elimina los bloques de notas de orador (::: {.notes}) del render,
-- SOLO cuando corre en el CI (GitHub Actions define CI=true): el sitio
-- público queda sin notas y sin su rastro en search.json, mientras los
-- renders locales del profesor (tecla S, panel) las conservan.
-- Regla de visibilidad del curso: las notas son material solo-profesor.

if os.getenv("CI") == nil then
  return {}
end

function Div(el)
  if el.classes:includes("notes") then
    return {}
  end
end
