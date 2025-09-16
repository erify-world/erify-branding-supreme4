import React from 'react'
import './StatCard.css'

interface StatCardProps {
  title: string
  value: string | number
  change?: string
  changeType?: 'positive' | 'negative' | 'neutral'
  icon?: string
  loading?: boolean
}

const StatCard: React.FC<StatCardProps> = ({
  title,
  value,
  change,
  changeType = 'neutral',
  icon,
  loading = false
}) => {
  if (loading) {
    return (
      <div className="stat-card stat-card--loading">
        <div className="stat-card__skeleton">
          <div className="stat-card__skeleton-line stat-card__skeleton-line--title"></div>
          <div className="stat-card__skeleton-line stat-card__skeleton-line--value"></div>
          <div className="stat-card__skeleton-line stat-card__skeleton-line--change"></div>
        </div>
      </div>
    )
  }

  return (
    <div className="stat-card">
      <div className="stat-card__header">
        {icon && <span className="stat-card__icon">{icon}</span>}
        <h3 className="stat-card__title">{title}</h3>
      </div>
      
      <div className="stat-card__body">
        <div className="stat-card__value">{value}</div>
        {change && (
          <div className={`stat-card__change stat-card__change--${changeType}`}>
            <span className="stat-card__change-indicator">
              {changeType === 'positive' ? '↗' : changeType === 'negative' ? '↘' : '→'}
            </span>
            {change}
          </div>
        )}
      </div>
    </div>
  )
}

export default StatCard