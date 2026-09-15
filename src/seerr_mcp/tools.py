"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/seerr_mcp/tools.py

One tool per operation, 170 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_auth_local(body: dict) -> str:
    """Sign in using a local account.

    POST /api/v1/auth/local

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/auth/local", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_auth_logout() -> str:
    """Sign out and clear session cookie.

    POST /api/v1/auth/logout
    """
    return call("POST", "/api/v1/auth/logout", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_auth_plex(body: dict) -> str:
    """Sign in using a Plex token.

    POST /api/v1/auth/plex

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/auth/plex", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_auth_reset_password(body: dict) -> str:
    """Send a reset password email.

    POST /api/v1/auth/reset-password

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/auth/reset-password", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_auth_reset_password_by_guid(guid: str, body: dict) -> str:
    """Reset the password for a user.

    POST /api/v1/auth/reset-password/{guid}

    Args:
        guid: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/auth/reset-password/{guid}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_issue(body: dict) -> str:
    """Create new issue.

    POST /api/v1/issue

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/issue", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_issue_by_issue_id_by_status(issue_id: str, status: str) -> str:
    """Update an issue's status.

    POST /api/v1/issue/{issueId}/{status}

    Args:
        issue_id: Issue ID
        status: New status
    """
    return call("POST", f"/api/v1/issue/{issue_id}/{status}", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_issue_by_issue_id_comment(issue_id: float, body: dict) -> str:
    """Create a comment.

    POST /api/v1/issue/{issueId}/comment

    Args:
        issue_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/issue/{issue_id}/comment", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_media_by_media_id_by_status(media_id: str, status: str, body: dict) -> str:
    """Update media status.

    POST /api/v1/media/{mediaId}/{status}

    Args:
        media_id: Media ID
        status: New status
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/media/{media_id}/{status}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_request(body: dict) -> str:
    """Create new request.

    POST /api/v1/request

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/request", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_request_by_request_id_by_status(request_id: str, status: str) -> str:
    """Update a request's status.

    POST /api/v1/request/{requestId}/{status}

    Args:
        request_id: Request ID
        status: New status
    """
    return call("POST", f"/api/v1/request/{request_id}/{status}", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_request_by_request_id_retry(request_id: str) -> str:
    """Retry failed request.

    POST /api/v1/request/{requestId}/retry

    Args:
        request_id: Request ID
    """
    return call("POST", f"/api/v1/request/{request_id}/retry", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_cache_by_cache_id_flush(cache_id: str) -> str:
    """Flush a specific cache.

    POST /api/v1/settings/cache/{cacheId}/flush

    Args:
        cache_id: Path parameter.
    """
    return call("POST", f"/api/v1/settings/cache/{cache_id}/flush", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_discover(body: dict) -> str:
    """Batch update all sliders.

    POST /api/v1/settings/discover

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/discover", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_discover_add(body: dict) -> str:
    """Add a new slider.

    POST /api/v1/settings/discover/add

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/discover/add", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_initialize() -> str:
    """Initialize application.

    POST /api/v1/settings/initialize
    """
    return call("POST", "/api/v1/settings/initialize", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_jobs_by_job_id_cancel(job_id: str) -> str:
    """Cancel a specific job.

    POST /api/v1/settings/jobs/{jobId}/cancel

    Args:
        job_id: Path parameter.
    """
    return call("POST", f"/api/v1/settings/jobs/{job_id}/cancel", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_jobs_by_job_id_run(job_id: str) -> str:
    """Invoke a specific job.

    POST /api/v1/settings/jobs/{jobId}/run

    Args:
        job_id: Path parameter.
    """
    return call("POST", f"/api/v1/settings/jobs/{job_id}/run", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_jobs_by_job_id_schedule(job_id: str, body: dict) -> str:
    """Modify job schedule.

    POST /api/v1/settings/jobs/{jobId}/schedule

    Args:
        job_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/settings/jobs/{job_id}/schedule", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_main(body: dict) -> str:
    """Update main settings.

    POST /api/v1/settings/main

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/main", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_main_regenerate() -> str:
    """Get main settings with newly-generated API key.

    POST /api/v1/settings/main/regenerate
    """
    return call("POST", "/api/v1/settings/main/regenerate", query=None, body=None)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_discord(body: dict) -> str:
    """Update Discord notification settings.

    POST /api/v1/settings/notifications/discord

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/discord", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_discord_test(body: dict) -> str:
    """Test Discord settings.

    POST /api/v1/settings/notifications/discord/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/discord/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_email(body: dict) -> str:
    """Update email notification settings.

    POST /api/v1/settings/notifications/email

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/email", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_email_test(body: dict) -> str:
    """Test email settings.

    POST /api/v1/settings/notifications/email/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/email/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_gotify(body: dict) -> str:
    """Update Gotify notification settings.

    POST /api/v1/settings/notifications/gotify

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/gotify", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_gotify_test(body: dict) -> str:
    """Test Gotify settings.

    POST /api/v1/settings/notifications/gotify/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/gotify/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_lunasea(body: dict) -> str:
    """Update LunaSea notification settings.

    POST /api/v1/settings/notifications/lunasea

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/lunasea", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_lunasea_test(body: dict) -> str:
    """Test LunaSea settings.

    POST /api/v1/settings/notifications/lunasea/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/lunasea/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_pushbullet(body: dict) -> str:
    """Update Pushbullet notification settings.

    POST /api/v1/settings/notifications/pushbullet

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/pushbullet", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_pushbullet_test(body: dict) -> str:
    """Test Pushbullet settings.

    POST /api/v1/settings/notifications/pushbullet/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/pushbullet/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_pushover(body: dict) -> str:
    """Update Pushover notification settings.

    POST /api/v1/settings/notifications/pushover

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/pushover", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_pushover_test(body: dict) -> str:
    """Test Pushover settings.

    POST /api/v1/settings/notifications/pushover/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/pushover/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_slack(body: dict) -> str:
    """Update Slack notification settings.

    POST /api/v1/settings/notifications/slack

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/slack", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_slack_test(body: dict) -> str:
    """Test Slack settings.

    POST /api/v1/settings/notifications/slack/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/slack/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_telegram(body: dict) -> str:
    """Update Telegram notification settings.

    POST /api/v1/settings/notifications/telegram

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/telegram", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_telegram_test(body: dict) -> str:
    """Test Telegram settings.

    POST /api/v1/settings/notifications/telegram/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/telegram/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_webhook(body: dict) -> str:
    """Update webhook notification settings.

    POST /api/v1/settings/notifications/webhook

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/webhook", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_webhook_test(body: dict) -> str:
    """Test webhook settings.

    POST /api/v1/settings/notifications/webhook/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/webhook/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_webpush(body: dict) -> str:
    """Update Web Push notification settings.

    POST /api/v1/settings/notifications/webpush

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/webpush", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_notifications_webpush_test(body: dict) -> str:
    """Test Web Push settings.

    POST /api/v1/settings/notifications/webpush/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/notifications/webpush/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_plex(body: dict) -> str:
    """Update Plex settings.

    POST /api/v1/settings/plex

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/plex", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_plex_sync(body: dict) -> str:
    """Start full Plex library scan.

    POST /api/v1/settings/plex/sync

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/plex/sync", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_radarr(body: dict) -> str:
    """Create Radarr instance.

    POST /api/v1/settings/radarr

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/radarr", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_radarr_test(body: dict) -> str:
    """Test Radarr configuration.

    POST /api/v1/settings/radarr/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/radarr/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_sonarr(body: dict) -> str:
    """Create Sonarr instance.

    POST /api/v1/settings/sonarr

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/sonarr", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_sonarr_test(body: dict) -> str:
    """Test Sonarr configuration.

    POST /api/v1/settings/sonarr/test

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/sonarr/test", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_settings_tautulli(body: dict) -> str:
    """Update Tautulli settings.

    POST /api/v1/settings/tautulli

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/settings/tautulli", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user(body: dict) -> str:
    """Create new user.

    POST /api/v1/user

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/user", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_by_user_id_settings_main(user_id: float, body: dict) -> str:
    """Update general settings for a user.

    POST /api/v1/user/{userId}/settings/main

    Args:
        user_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/user/{user_id}/settings/main", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_by_user_id_settings_notifications(user_id: float, body: dict) -> str:
    """Update notification settings for a user.

    POST /api/v1/user/{userId}/settings/notifications

    Args:
        user_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/user/{user_id}/settings/notifications", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_by_user_id_settings_password(user_id: float, body: dict) -> str:
    """Update password for a user.

    POST /api/v1/user/{userId}/settings/password

    Args:
        user_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/user/{user_id}/settings/password", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_by_user_id_settings_permissions(user_id: float, body: dict) -> str:
    """Update permission settings for a user.

    POST /api/v1/user/{userId}/settings/permissions

    Args:
        user_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/api/v1/user/{user_id}/settings/permissions", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_import_from_plex(body: dict) -> str:
    """Import all users from Plex.

    POST /api/v1/user/import-from-plex

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/user/import-from-plex", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def create_user_register_push_subscription(body: dict) -> str:
    """Register a web push /user/registerPushSubscription.

    POST /api/v1/user/registerPushSubscription

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/api/v1/user/registerPushSubscription", query=None, body=body)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_issue_by_issue_id(issue_id: str) -> str:
    """Delete issue.

    DELETE /api/v1/issue/{issueId}

    Args:
        issue_id: Issue ID
    """
    return call("DELETE", f"/api/v1/issue/{issue_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_issue_comment_by_comment_id(comment_id: str) -> str:
    """Delete issue comment.

    DELETE /api/v1/issueComment/{commentId}

    Args:
        comment_id: Issue Comment ID
    """
    return call("DELETE", f"/api/v1/issueComment/{comment_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_by_media_id(media_id: str) -> str:
    """Delete media item.

    DELETE /api/v1/media/{mediaId}

    Args:
        media_id: Media ID
    """
    return call("DELETE", f"/api/v1/media/{media_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_request_by_request_id(request_id: str) -> str:
    """Delete request.

    DELETE /api/v1/request/{requestId}

    Args:
        request_id: Request ID
    """
    return call("DELETE", f"/api/v1/request/{request_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_settings_discover_by_slider_id(slider_id: float) -> str:
    """Delete slider by ID.

    DELETE /api/v1/settings/discover/{sliderId}

    Args:
        slider_id: Path parameter.
    """
    return call("DELETE", f"/api/v1/settings/discover/{slider_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_settings_radarr_by_radarr_id(radarr_id: int) -> str:
    """Delete Radarr instance.

    DELETE /api/v1/settings/radarr/{radarrId}

    Args:
        radarr_id: Radarr instance ID
    """
    return call("DELETE", f"/api/v1/settings/radarr/{radarr_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_settings_sonarr_by_sonarr_id(sonarr_id: int) -> str:
    """Delete Sonarr instance.

    DELETE /api/v1/settings/sonarr/{sonarrId}

    Args:
        sonarr_id: Sonarr instance ID
    """
    return call("DELETE", f"/api/v1/settings/sonarr/{sonarr_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_user_by_user_id(user_id: float) -> str:
    """Delete user by ID.

    DELETE /api/v1/user/{userId}

    Args:
        user_id: Path parameter.
    """
    return call("DELETE", f"/api/v1/user/{user_id}", query=None, body=None)


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_user_by_user_id_push_subscription_by_endpoint(user_id: float, endpoint: str) -> str:
    """Delete user push subscription by key.

    DELETE /api/v1/user/{userId}/pushSubscription/{endpoint}

    Args:
        user_id: Path parameter.
        endpoint: Path parameter.
    """
    return call("DELETE", f"/api/v1/user/{user_id}/pushSubscription/{endpoint}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_collection_by_collection_id(collection_id: float, language: str | None = None) -> str:
    """Get collection details.

    GET /api/v1/collection/{collectionId}

    Args:
        collection_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/collection/{collection_id}", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_keyword_by_keyword_id_movies(keyword_id: float, page: float | None = None, language: str | None = None) -> str:
    """Get movies from keyword.

    GET /api/v1/discover/keyword/{keywordId}/movies

    Args:
        keyword_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/discover/keyword/{keyword_id}/movies", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_movies_genre_by_genre_id(genre_id: str, page: float | None = None, language: str | None = None) -> str:
    """Discover movies by genre.

    GET /api/v1/discover/movies/genre/{genreId}

    Args:
        genre_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/discover/movies/genre/{genre_id}", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_movies_language_by_language(language: str, page: float | None = None, language_query: str | None = None) -> str:
    """Discover movies by original language.

    GET /api/v1/discover/movies/language/{language}

    Args:
        language: Path parameter.
        page: Query parameter.
        language_query: Query parameter.
    """
    return call("GET", f"/api/v1/discover/movies/language/{language}", query={"page": page, "language": language_query}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_movies_studio_by_studio_id(studio_id: str, page: float | None = None, language: str | None = None) -> str:
    """Discover movies by studio.

    GET /api/v1/discover/movies/studio/{studioId}

    Args:
        studio_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/discover/movies/studio/{studio_id}", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_tv_genre_by_genre_id(genre_id: str, page: float | None = None, language: str | None = None) -> str:
    """Discover TV shows by genre.

    GET /api/v1/discover/tv/genre/{genreId}

    Args:
        genre_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/discover/tv/genre/{genre_id}", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_tv_language_by_language(language: str, page: float | None = None, language_query: str | None = None) -> str:
    """Discover TV shows by original language.

    GET /api/v1/discover/tv/language/{language}

    Args:
        language: Path parameter.
        page: Query parameter.
        language_query: Query parameter.
    """
    return call("GET", f"/api/v1/discover/tv/language/{language}", query={"page": page, "language": language_query}, body=None)


@mcp.tool(annotations=_READ)
def get_discover_tv_network_by_network_id(network_id: str, page: float | None = None, language: str | None = None) -> str:
    """Discover TV shows by network.

    GET /api/v1/discover/tv/network/{networkId}

    Args:
        network_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/discover/tv/network/{network_id}", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_issue_by_issue_id(issue_id: float) -> str:
    """Get issue.

    GET /api/v1/issue/{issueId}

    Args:
        issue_id: Path parameter.
    """
    return call("GET", f"/api/v1/issue/{issue_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_issue_comment_by_comment_id(comment_id: str) -> str:
    """Get issue comment.

    GET /api/v1/issueComment/{commentId}

    Args:
        comment_id: Path parameter.
    """
    return call("GET", f"/api/v1/issueComment/{comment_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_keyword_by_keyword_id(keyword_id: float) -> str:
    """Get keyword.

    GET /api/v1/keyword/{keywordId}

    Args:
        keyword_id: Path parameter.
    """
    return call("GET", f"/api/v1/keyword/{keyword_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_media_by_media_id_watch_data(media_id: str) -> str:
    """Get watch data.

    GET /api/v1/media/{mediaId}/watch_data

    Args:
        media_id: Media ID
    """
    return call("GET", f"/api/v1/media/{media_id}/watch_data", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_movie_id(movie_id: float, language: str | None = None) -> str:
    """Get movie details.

    GET /api/v1/movie/{movieId}

    Args:
        movie_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/movie/{movie_id}", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_movie_id_ratings(movie_id: float) -> str:
    """Get movie ratings.

    GET /api/v1/movie/{movieId}/ratings

    Args:
        movie_id: Path parameter.
    """
    return call("GET", f"/api/v1/movie/{movie_id}/ratings", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_movie_id_ratingscombined(movie_id: float) -> str:
    """Get RT and IMDB movie ratings combined.

    GET /api/v1/movie/{movieId}/ratingscombined

    Args:
        movie_id: Path parameter.
    """
    return call("GET", f"/api/v1/movie/{movie_id}/ratingscombined", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_movie_id_recommendations(movie_id: float, page: float | None = None, language: str | None = None) -> str:
    """Get recommended movies.

    GET /api/v1/movie/{movieId}/recommendations

    Args:
        movie_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/movie/{movie_id}/recommendations", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_movie_by_movie_id_similar(movie_id: float, page: float | None = None, language: str | None = None) -> str:
    """Get similar movies.

    GET /api/v1/movie/{movieId}/similar

    Args:
        movie_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/movie/{movie_id}/similar", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_network_by_network_id(network_id: float) -> str:
    """Get TV network details.

    GET /api/v1/network/{networkId}

    Args:
        network_id: Path parameter.
    """
    return call("GET", f"/api/v1/network/{network_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_person_by_person_id(person_id: float, language: str | None = None) -> str:
    """Get person details.

    GET /api/v1/person/{personId}

    Args:
        person_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/person/{person_id}", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_person_by_person_id_combined_credits(person_id: float, language: str | None = None) -> str:
    """Get combined credits.

    GET /api/v1/person/{personId}/combined_credits

    Args:
        person_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/person/{person_id}/combined_credits", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_request_by_request_id(request_id: str) -> str:
    """Get MediaRequest.

    GET /api/v1/request/{requestId}

    Args:
        request_id: Request ID
    """
    return call("GET", f"/api/v1/request/{request_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_service_radarr_by_radarr_id(radarr_id: float) -> str:
    """Get Radarr server quality profiles and root folders.

    GET /api/v1/service/radarr/{radarrId}

    Args:
        radarr_id: Path parameter.
    """
    return call("GET", f"/api/v1/service/radarr/{radarr_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_service_sonarr_by_sonarr_id(sonarr_id: float) -> str:
    """Get Sonarr server quality profiles and root folders.

    GET /api/v1/service/sonarr/{sonarrId}

    Args:
        sonarr_id: Path parameter.
    """
    return call("GET", f"/api/v1/service/sonarr/{sonarr_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_service_sonarr_lookup_by_tmdb_id(tmdb_id: float) -> str:
    """Get series from Sonarr.

    GET /api/v1/service/sonarr/lookup/{tmdbId}

    Args:
        tmdb_id: Path parameter.
    """
    return call("GET", f"/api/v1/service/sonarr/lookup/{tmdb_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_settings_radarr_by_radarr_id_profiles(radarr_id: int) -> str:
    """Get available Radarr profiles.

    GET /api/v1/settings/radarr/{radarrId}/profiles

    Args:
        radarr_id: Radarr instance ID
    """
    return call("GET", f"/api/v1/settings/radarr/{radarr_id}/profiles", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_studio_by_studio_id(studio_id: float) -> str:
    """Get movie studio details.

    GET /api/v1/studio/{studioId}

    Args:
        studio_id: Path parameter.
    """
    return call("GET", f"/api/v1/studio/{studio_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_tv_by_tv_id(tv_id: float, language: str | None = None) -> str:
    """Get TV details.

    GET /api/v1/tv/{tvId}

    Args:
        tv_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/tv/{tv_id}", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_tv_by_tv_id_ratings(tv_id: float) -> str:
    """Get TV ratings.

    GET /api/v1/tv/{tvId}/ratings

    Args:
        tv_id: Path parameter.
    """
    return call("GET", f"/api/v1/tv/{tv_id}/ratings", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_tv_by_tv_id_recommendations(tv_id: float, page: float | None = None, language: str | None = None) -> str:
    """Get recommended TV series.

    GET /api/v1/tv/{tvId}/recommendations

    Args:
        tv_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/tv/{tv_id}/recommendations", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_tv_by_tv_id_season_by_season_id(tv_id: float, season_id: float, language: str | None = None) -> str:
    """Get season details and episode list.

    GET /api/v1/tv/{tvId}/season/{seasonId}

    Args:
        tv_id: Path parameter.
        season_id: Path parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/tv/{tv_id}/season/{season_id}", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_tv_by_tv_id_similar(tv_id: float, page: float | None = None, language: str | None = None) -> str:
    """Get similar TV series.

    GET /api/v1/tv/{tvId}/similar

    Args:
        tv_id: Path parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", f"/api/v1/tv/{tv_id}/similar", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id(user_id: float) -> str:
    """Get user by ID.

    GET /api/v1/user/{userId}

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_push_subscription_by_endpoint(user_id: float, endpoint: str) -> str:
    """Get web push notification settings for a user.

    GET /api/v1/user/{userId}/pushSubscription/{endpoint}

    Args:
        user_id: Path parameter.
        endpoint: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/pushSubscription/{endpoint}", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_push_subscriptions(user_id: float) -> str:
    """Get all web push notification settings for a user.

    GET /api/v1/user/{userId}/pushSubscriptions

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/pushSubscriptions", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_quota(user_id: float) -> str:
    """Get quotas for a specific user.

    GET /api/v1/user/{userId}/quota

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/quota", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_requests(user_id: float, take: float | None = None, skip: float | None = None) -> str:
    """Get requests for a specific user.

    GET /api/v1/user/{userId}/requests

    Args:
        user_id: Path parameter.
        take: Query parameter.
        skip: Query parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/requests", query={"take": take, "skip": skip}, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_settings_main(user_id: float) -> str:
    """Get general settings for a user.

    GET /api/v1/user/{userId}/settings/main

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/settings/main", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_settings_notifications(user_id: float) -> str:
    """Get notification settings for a user.

    GET /api/v1/user/{userId}/settings/notifications

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/settings/notifications", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_settings_password(user_id: float) -> str:
    """Get password page informatiom.

    GET /api/v1/user/{userId}/settings/password

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/settings/password", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_settings_permissions(user_id: float) -> str:
    """Get permission settings for a user.

    GET /api/v1/user/{userId}/settings/permissions

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/settings/permissions", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_watch_data(user_id: float) -> str:
    """Get watch data.

    GET /api/v1/user/{userId}/watch_data

    Args:
        user_id: Path parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/watch_data", query=None, body=None)


@mcp.tool(annotations=_READ)
def get_user_by_user_id_watchlist(user_id: float, page: float | None = None) -> str:
    """Get the Plex watchlist for a specific user.

    GET /api/v1/user/{userId}/watchlist

    Args:
        user_id: Path parameter.
        page: Query parameter.
    """
    return call("GET", f"/api/v1/user/{user_id}/watchlist", query={"page": page}, body=None)


@mcp.tool(annotations=_READ)
def list_auth_me() -> str:
    """Get logged-in user.

    GET /api/v1/auth/me
    """
    return call("GET", "/api/v1/auth/me", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_backdrops() -> str:
    """Get backdrops of trending items.

    GET /api/v1/backdrops
    """
    return call("GET", "/api/v1/backdrops", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_discover_genreslider_movie(language: str | None = None) -> str:
    """Get genre slider data for movies.

    GET /api/v1/discover/genreslider/movie

    Args:
        language: Query parameter.
    """
    return call("GET", "/api/v1/discover/genreslider/movie", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_genreslider_tv(language: str | None = None) -> str:
    """Get genre slider data for TV series.

    GET /api/v1/discover/genreslider/tv

    Args:
        language: Query parameter.
    """
    return call("GET", "/api/v1/discover/genreslider/tv", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_movies(page: float | None = None, language: str | None = None, genre: str | None = None, studio: float | None = None, keywords: str | None = None, sort_by: str | None = None, primary_release_date_gte: str | None = None, primary_release_date_lte: str | None = None, with_runtime_gte: float | None = None, with_runtime_lte: float | None = None, vote_average_gte: float | None = None, vote_average_lte: float | None = None, vote_count_gte: float | None = None, vote_count_lte: float | None = None, watch_region: str | None = None, watch_providers: str | None = None) -> str:
    """Discover movies.

    GET /api/v1/discover/movies

    Args:
        page: Query parameter.
        language: Query parameter.
        genre: Query parameter.
        studio: Query parameter.
        keywords: Query parameter.
        sort_by: Query parameter.
        primary_release_date_gte: Query parameter.
        primary_release_date_lte: Query parameter.
        with_runtime_gte: Query parameter.
        with_runtime_lte: Query parameter.
        vote_average_gte: Query parameter.
        vote_average_lte: Query parameter.
        vote_count_gte: Query parameter.
        vote_count_lte: Query parameter.
        watch_region: Query parameter.
        watch_providers: Query parameter.
    """
    return call("GET", "/api/v1/discover/movies", query={"page": page, "language": language, "genre": genre, "studio": studio, "keywords": keywords, "sortBy": sort_by, "primaryReleaseDateGte": primary_release_date_gte, "primaryReleaseDateLte": primary_release_date_lte, "withRuntimeGte": with_runtime_gte, "withRuntimeLte": with_runtime_lte, "voteAverageGte": vote_average_gte, "voteAverageLte": vote_average_lte, "voteCountGte": vote_count_gte, "voteCountLte": vote_count_lte, "watchRegion": watch_region, "watchProviders": watch_providers}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_movies_upcoming(page: float | None = None, language: str | None = None) -> str:
    """Upcoming movies.

    GET /api/v1/discover/movies/upcoming

    Args:
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", "/api/v1/discover/movies/upcoming", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_trending(page: float | None = None, language: str | None = None) -> str:
    """Trending movies and TV.

    GET /api/v1/discover/trending

    Args:
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", "/api/v1/discover/trending", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_tv(page: float | None = None, language: str | None = None, genre: str | None = None, network: float | None = None, keywords: str | None = None, sort_by: str | None = None, first_air_date_gte: str | None = None, first_air_date_lte: str | None = None, with_runtime_gte: float | None = None, with_runtime_lte: float | None = None, vote_average_gte: float | None = None, vote_average_lte: float | None = None, vote_count_gte: float | None = None, vote_count_lte: float | None = None, watch_region: str | None = None, watch_providers: str | None = None) -> str:
    """Discover TV shows.

    GET /api/v1/discover/tv

    Args:
        page: Query parameter.
        language: Query parameter.
        genre: Query parameter.
        network: Query parameter.
        keywords: Query parameter.
        sort_by: Query parameter.
        first_air_date_gte: Query parameter.
        first_air_date_lte: Query parameter.
        with_runtime_gte: Query parameter.
        with_runtime_lte: Query parameter.
        vote_average_gte: Query parameter.
        vote_average_lte: Query parameter.
        vote_count_gte: Query parameter.
        vote_count_lte: Query parameter.
        watch_region: Query parameter.
        watch_providers: Query parameter.
    """
    return call("GET", "/api/v1/discover/tv", query={"page": page, "language": language, "genre": genre, "network": network, "keywords": keywords, "sortBy": sort_by, "firstAirDateGte": first_air_date_gte, "firstAirDateLte": first_air_date_lte, "withRuntimeGte": with_runtime_gte, "withRuntimeLte": with_runtime_lte, "voteAverageGte": vote_average_gte, "voteAverageLte": vote_average_lte, "voteCountGte": vote_count_gte, "voteCountLte": vote_count_lte, "watchRegion": watch_region, "watchProviders": watch_providers}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_tv_upcoming(page: float | None = None, language: str | None = None) -> str:
    """Discover Upcoming TV shows.

    GET /api/v1/discover/tv/upcoming

    Args:
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", "/api/v1/discover/tv/upcoming", query={"page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_discover_watchlist(page: float | None = None) -> str:
    """Get the Plex watchlist.

    GET /api/v1/discover/watchlist

    Args:
        page: Query parameter.
    """
    return call("GET", "/api/v1/discover/watchlist", query={"page": page}, body=None)


@mcp.tool(annotations=_READ)
def list_genres_movie(language: str | None = None) -> str:
    """Get list of official TMDB movie genres.

    GET /api/v1/genres/movie

    Args:
        language: Query parameter.
    """
    return call("GET", "/api/v1/genres/movie", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_genres_tv(language: str | None = None) -> str:
    """Get list of official TMDB movie genres.

    GET /api/v1/genres/tv

    Args:
        language: Query parameter.
    """
    return call("GET", "/api/v1/genres/tv", query={"language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_issue(take: float | None = None, skip: float | None = None, sort: str | None = None, filter_: str | None = None, requested_by: float | None = None) -> str:
    """Get all issues.

    GET /api/v1/issue

    Args:
        take: Query parameter.
        skip: Query parameter.
        sort: Query parameter.
        filter_: Query parameter.
        requested_by: Query parameter.
    """
    return call("GET", "/api/v1/issue", query={"take": take, "skip": skip, "sort": sort, "filter": filter_, "requestedBy": requested_by}, body=None)


@mcp.tool(annotations=_READ)
def list_issue_count() -> str:
    """Gets issue counts.

    GET /api/v1/issue/count
    """
    return call("GET", "/api/v1/issue/count", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_languages() -> str:
    """Languages supported by TMDB.

    GET /api/v1/languages
    """
    return call("GET", "/api/v1/languages", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_media(take: float | None = None, skip: float | None = None, filter_: str | None = None, sort: str | None = None) -> str:
    """Get media.

    GET /api/v1/media

    Args:
        take: Query parameter.
        skip: Query parameter.
        filter_: Query parameter.
        sort: Query parameter.
    """
    return call("GET", "/api/v1/media", query={"take": take, "skip": skip, "filter": filter_, "sort": sort}, body=None)


@mcp.tool(annotations=_READ)
def list_regions() -> str:
    """Regions supported by TMDB.

    GET /api/v1/regions
    """
    return call("GET", "/api/v1/regions", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_request(take: float | None = None, skip: float | None = None, filter_: str | None = None, sort: str | None = None, requested_by: float | None = None) -> str:
    """Get all requests.

    GET /api/v1/request

    Args:
        take: Query parameter.
        skip: Query parameter.
        filter_: Query parameter.
        sort: Query parameter.
        requested_by: Query parameter.
    """
    return call("GET", "/api/v1/request", query={"take": take, "skip": skip, "filter": filter_, "sort": sort, "requestedBy": requested_by}, body=None)


@mcp.tool(annotations=_READ)
def list_request_count() -> str:
    """Gets request counts.

    GET /api/v1/request/count
    """
    return call("GET", "/api/v1/request/count", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_search(query: str | None = None, page: float | None = None, language: str | None = None) -> str:
    """Search for movies, TV shows, or people.

    GET /api/v1/search

    Args:
        query: Query parameter.
        page: Query parameter.
        language: Query parameter.
    """
    return call("GET", "/api/v1/search", query={"query": query, "page": page, "language": language}, body=None)


@mcp.tool(annotations=_READ)
def list_search_company(query: str | None = None, page: float | None = None) -> str:
    """Search for companies.

    GET /api/v1/search/company

    Args:
        query: Query parameter.
        page: Query parameter.
    """
    return call("GET", "/api/v1/search/company", query={"query": query, "page": page}, body=None)


@mcp.tool(annotations=_READ)
def list_search_keyword(query: str | None = None, page: float | None = None) -> str:
    """Search for keywords.

    GET /api/v1/search/keyword

    Args:
        query: Query parameter.
        page: Query parameter.
    """
    return call("GET", "/api/v1/search/keyword", query={"query": query, "page": page}, body=None)


@mcp.tool(annotations=_READ)
def list_service_radarr() -> str:
    """Get non-sensitive Radarr server list.

    GET /api/v1/service/radarr
    """
    return call("GET", "/api/v1/service/radarr", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_service_sonarr() -> str:
    """Get non-sensitive Sonarr server list.

    GET /api/v1/service/sonarr
    """
    return call("GET", "/api/v1/service/sonarr", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_about() -> str:
    """Get server stats.

    GET /api/v1/settings/about
    """
    return call("GET", "/api/v1/settings/about", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_cache() -> str:
    """Get a list of active caches.

    GET /api/v1/settings/cache
    """
    return call("GET", "/api/v1/settings/cache", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_discover() -> str:
    """Get all discover sliders.

    GET /api/v1/settings/discover
    """
    return call("GET", "/api/v1/settings/discover", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_discover_reset() -> str:
    """Reset all discover sliders.

    GET /api/v1/settings/discover/reset
    """
    return call("GET", "/api/v1/settings/discover/reset", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_jobs() -> str:
    """Get scheduled jobs.

    GET /api/v1/settings/jobs
    """
    return call("GET", "/api/v1/settings/jobs", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_logs(take: float | None = None, skip: float | None = None, filter_: str | None = None, search: str | None = None) -> str:
    """Returns logs.

    GET /api/v1/settings/logs

    Args:
        take: Query parameter.
        skip: Query parameter.
        filter_: Query parameter.
        search: Query parameter.
    """
    return call("GET", "/api/v1/settings/logs", query={"take": take, "skip": skip, "filter": filter_, "search": search}, body=None)


@mcp.tool(annotations=_READ)
def list_settings_main() -> str:
    """Get main settings.

    GET /api/v1/settings/main
    """
    return call("GET", "/api/v1/settings/main", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_discord() -> str:
    """Get Discord notification settings.

    GET /api/v1/settings/notifications/discord
    """
    return call("GET", "/api/v1/settings/notifications/discord", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_email() -> str:
    """Get email notification settings.

    GET /api/v1/settings/notifications/email
    """
    return call("GET", "/api/v1/settings/notifications/email", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_gotify() -> str:
    """Get Gotify notification settings.

    GET /api/v1/settings/notifications/gotify
    """
    return call("GET", "/api/v1/settings/notifications/gotify", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_lunasea() -> str:
    """Get LunaSea notification settings.

    GET /api/v1/settings/notifications/lunasea
    """
    return call("GET", "/api/v1/settings/notifications/lunasea", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_pushbullet() -> str:
    """Get Pushbullet notification settings.

    GET /api/v1/settings/notifications/pushbullet
    """
    return call("GET", "/api/v1/settings/notifications/pushbullet", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_pushover() -> str:
    """Get Pushover notification settings.

    GET /api/v1/settings/notifications/pushover
    """
    return call("GET", "/api/v1/settings/notifications/pushover", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_pushover_sounds(token: str | None = None) -> str:
    """Get Pushover sounds.

    GET /api/v1/settings/notifications/pushover/sounds

    Args:
        token: Query parameter.
    """
    return call("GET", "/api/v1/settings/notifications/pushover/sounds", query={"token": token}, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_slack() -> str:
    """Get Slack notification settings.

    GET /api/v1/settings/notifications/slack
    """
    return call("GET", "/api/v1/settings/notifications/slack", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_telegram() -> str:
    """Get Telegram notification settings.

    GET /api/v1/settings/notifications/telegram
    """
    return call("GET", "/api/v1/settings/notifications/telegram", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_webhook() -> str:
    """Get webhook notification settings.

    GET /api/v1/settings/notifications/webhook
    """
    return call("GET", "/api/v1/settings/notifications/webhook", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_notifications_webpush() -> str:
    """Get Web Push notification settings.

    GET /api/v1/settings/notifications/webpush
    """
    return call("GET", "/api/v1/settings/notifications/webpush", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_plex() -> str:
    """Get Plex settings.

    GET /api/v1/settings/plex
    """
    return call("GET", "/api/v1/settings/plex", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_plex_devices_servers() -> str:
    """Gets the user's available Plex servers.

    GET /api/v1/settings/plex/devices/servers
    """
    return call("GET", "/api/v1/settings/plex/devices/servers", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_plex_library(sync: str | None = None, enable: str | None = None) -> str:
    """Get Plex libraries.

    GET /api/v1/settings/plex/library

    Args:
        sync: Syncs the current libraries with the current Plex server
        enable: Comma separated list of libraries to enable. Any libraries not passed will be disabled!
    """
    return call("GET", "/api/v1/settings/plex/library", query={"sync": sync, "enable": enable}, body=None)


@mcp.tool(annotations=_READ)
def list_settings_plex_sync() -> str:
    """Get status of full Plex library scan.

    GET /api/v1/settings/plex/sync
    """
    return call("GET", "/api/v1/settings/plex/sync", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_plex_users() -> str:
    """Get Plex users.

    GET /api/v1/settings/plex/users
    """
    return call("GET", "/api/v1/settings/plex/users", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_public() -> str:
    """Get public settings.

    GET /api/v1/settings/public
    """
    return call("GET", "/api/v1/settings/public", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_radarr() -> str:
    """Get Radarr settings.

    GET /api/v1/settings/radarr
    """
    return call("GET", "/api/v1/settings/radarr", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_sonarr() -> str:
    """Get Sonarr settings.

    GET /api/v1/settings/sonarr
    """
    return call("GET", "/api/v1/settings/sonarr", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_settings_tautulli() -> str:
    """Get Tautulli settings.

    GET /api/v1/settings/tautulli
    """
    return call("GET", "/api/v1/settings/tautulli", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_status() -> str:
    """Get Overseerr status.

    GET /api/v1/status
    """
    return call("GET", "/api/v1/status", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_status_appdata() -> str:
    """Get application data volume status.

    GET /api/v1/status/appdata
    """
    return call("GET", "/api/v1/status/appdata", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_user(take: float | None = None, skip: float | None = None, sort: str | None = None) -> str:
    """Get all users.

    GET /api/v1/user

    Args:
        take: Query parameter.
        skip: Query parameter.
        sort: Query parameter.
    """
    return call("GET", "/api/v1/user", query={"take": take, "skip": skip, "sort": sort}, body=None)


@mcp.tool(annotations=_READ)
def list_watchproviders_movies(watch_region: str | None = None) -> str:
    """Get watch provider movies.

    GET /api/v1/watchproviders/movies

    Args:
        watch_region: Query parameter.
    """
    return call("GET", "/api/v1/watchproviders/movies", query={"watchRegion": watch_region}, body=None)


@mcp.tool(annotations=_READ)
def list_watchproviders_regions() -> str:
    """Get watch provider regions.

    GET /api/v1/watchproviders/regions
    """
    return call("GET", "/api/v1/watchproviders/regions", query=None, body=None)


@mcp.tool(annotations=_READ)
def list_watchproviders_tv(watch_region: str | None = None) -> str:
    """Get watch provider series.

    GET /api/v1/watchproviders/tv

    Args:
        watch_region: Query parameter.
    """
    return call("GET", "/api/v1/watchproviders/tv", query={"watchRegion": watch_region}, body=None)


@mcp.tool(annotations=_WRITE)
def update_issue_comment_by_comment_id(comment_id: str, body: dict) -> str:
    """Update issue comment.

    PUT /api/v1/issueComment/{commentId}

    Args:
        comment_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/issueComment/{comment_id}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_request_by_request_id(request_id: str, body: dict) -> str:
    """Update MediaRequest.

    PUT /api/v1/request/{requestId}

    Args:
        request_id: Request ID
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/request/{request_id}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_settings_discover_by_slider_id(slider_id: float, body: dict) -> str:
    """Update a single slider.

    PUT /api/v1/settings/discover/{sliderId}

    Args:
        slider_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/settings/discover/{slider_id}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_settings_radarr_by_radarr_id(radarr_id: int, body: dict) -> str:
    """Update Radarr instance.

    PUT /api/v1/settings/radarr/{radarrId}

    Args:
        radarr_id: Radarr instance ID
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/settings/radarr/{radarr_id}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_settings_sonarr_by_sonarr_id(sonarr_id: int, body: dict) -> str:
    """Update Sonarr instance.

    PUT /api/v1/settings/sonarr/{sonarrId}

    Args:
        sonarr_id: Sonarr instance ID
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/settings/sonarr/{sonarr_id}", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_user(body: dict) -> str:
    """Update batch of users.

    PUT /api/v1/user

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/api/v1/user", query=None, body=body)


@mcp.tool(annotations=_WRITE)
def update_user_by_user_id(user_id: float, body: dict) -> str:
    """Update a user by user ID.

    PUT /api/v1/user/{userId}

    Args:
        user_id: Path parameter.
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", f"/api/v1/user/{user_id}", query=None, body=body)
