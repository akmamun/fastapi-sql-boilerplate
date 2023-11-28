
from typing import Optional
from fastapi import Query
from sqlalchemy import  asc, desc
from sqlalchemy.ext.asyncio import AsyncSession

async def paginate(
    session: AsyncSession,
    query,
    limit: Optional[int] = Query(10, description="Number of items per page", gt=0),
    offset: Optional[int] = Query(0, description="Number of items to skip", ge=0),
    sort_by: Optional[str] = Query("id", description="Column to sort by"),
    sort_desc: Optional[bool] = Query(False, description="Sort in descending order"),
):
    if sort_by:
        column = getattr(query.column_descriptions[0]['entity'], sort_by)
        if sort_desc:
            query = query.order_by(desc(column))
        else:
            query = query.order_by(asc(column))

    # Execute the query with pagination
    result = await session.execute(query.offset(offset).limit(limit))
    return result.scalars().all()