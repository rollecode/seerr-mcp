<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Seerr MCP server

<img style="justify-content:center;text-align: center;width: 95px; height: auto;" width="793" height="411" alt="image" src="https://github.com/user-attachments/assets/abed1a04-d69b-4ab4-a490-d606064df72d" />
<img style="justify-content:center;text-align: center;width: 49px; height: auto;" alt="Overseerr" src="public/logo.png" />

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Overseerr](https://img.shields.io/badge/Overseerr-5A67D8?style=for-the-badge&logo=overseerr&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-170%2F170-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Run Overseerr or Jellyseerr from Claude.ai and Claude Code. All 170 operations of the API are tools, generated from Overseerr's own OpenAPI document. Not a curated subset: every endpoint the web interface can reach, this can reach.

Jellyseerr is a fork of Overseerr and keeps the same API, so this works against either. Point `SEERR_URL` at whichever you run.

<hr>

## Why not the other options

Measured against `overseerr-api.yml`, which has 134 paths and 170 operations:

| Server | Overseerr tools | Coverage |
| --- | --- | --- |
| `davidgibbons/mcp-arr` (jellyseerr) | 9 | 5 % |
| `cyanheads/seerr-mcp-server` | search, availability, request | partial |
| `aserper/jellyseerr-mcp`, `ptbsare/overseerr-mcp-server` | request-centric subsets | partial |
| This one | **170** | **100 %** |

Every existing server treats Seerr as a request box: search, request, approve. Nothing else exposes the settings tree, user quotas and permissions, issues, the Plex and Sonarr/Radarr service configuration, discovery sliders or the job scheduler.

## How it stays complete

`src/seerr_mcp/tools.py` is generated, not written:

```bash
curl -o overseerr-api.yml https://raw.githubusercontent.com/sct/overseerr/develop/overseerr-api.yml
python scripts/convert_spec.py overseerr-api.yml openapi.json
python scripts/generate_tools.py openapi.json src/seerr_mcp/tools.py
```

A test compares every generated call against every operation in the spec, in both directions. An endpoint Overseerr adds and this misses fails the build; so does a tool pointing at an endpoint the spec does not define.

## Tool names

Verb first, derived from the method and path, so the name says what it does:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_request`, `list_issue` |
| `get_*_by_id` | Read one record | `get_movie_by_movie_id` |
| `create_*` | POST | `create_request`, `create_auth_local` |
| `update_*` | PUT | `update_settings_main` |
| `delete_*` | DELETE | `delete_request_by_request_id` |

170 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## What is covered

Every tag in the spec: `public`, `auth`, `users`, `search`, `request`, `movies`, `tv`, `person`, `media`, `collection`, `service`, `settings`, `issue`, `other`. That includes the whole settings tree (Plex, Radarr, Sonarr, Jellyfin, notifications, network, logs, jobs, cache), user permissions and quotas, watchlists, blacklists, discovery sliders and the issue tracker.

## Setup

```bash
git clone https://github.com/rollecode/seerr-mcp.git
cd seerr-mcp
uv venv && uv pip install -e .
```

```bash
export SEERR_URL=http://127.0.0.1:5055
export SEERR_API_KEY=...   # Settings, General, API Key
```

### Claude Code

```bash
claude mcp add seerr -- /path/to/seerr-mcp/.venv/bin/seerr-mcp
```

## Writing records

Settings endpoints replace the whole object, so read the matching `list_*` first, change the fields you want and send it all back as `body`.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

